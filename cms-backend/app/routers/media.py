import os
import uuid

from fastapi import APIRouter, Depends, HTTPException, UploadFile, File, Form
from sqlalchemy.orm import Session

from app.core.config import settings
from app.core.database import get_db
from app.core.security import get_current_user
from app.models.media import Media
from app.schemas.media import MediaOut

router = APIRouter(prefix="/api/media", tags=["media"])

ALLOWED_EXT = {".jpg", ".jpeg", ".png", ".webp", ".gif", ".svg"}


@router.get("", response_model=list[MediaOut])
def list_media(db: Session = Depends(get_db), _admin=Depends(get_current_user)):
    return db.query(Media).order_by(Media.created_at.desc()).all()


@router.post("/upload", response_model=MediaOut, status_code=201)
async def upload_media(
    file: UploadFile = File(...),
    alt: str = Form(""),
    db: Session = Depends(get_db),
    _admin=Depends(get_current_user),
):
    ext = os.path.splitext(file.filename or "")[1].lower()
    if ext not in ALLOWED_EXT:
        raise HTTPException(status_code=400, detail=f"Unsupported file type: {ext}")

    contents = await file.read()
    max_bytes = settings.max_upload_mb * 1024 * 1024
    if len(contents) > max_bytes:
        raise HTTPException(status_code=400, detail=f"File too large (max {settings.max_upload_mb}MB)")

    stored_name = f"{uuid.uuid4().hex}{ext}"
    dest_path = os.path.join(settings.upload_dir, stored_name)
    with open(dest_path, "wb") as f:
        f.write(contents)

    url = f"/uploads/{stored_name}"
    media = Media(filename=file.filename or stored_name, url=url, alt=alt)
    db.add(media)
    db.commit()
    db.refresh(media)
    return media


@router.delete("/{media_id}", status_code=204)
def delete_media(media_id: int, db: Session = Depends(get_db), _admin=Depends(get_current_user)):
    media = db.get(Media, media_id)
    if not media:
        raise HTTPException(status_code=404, detail="Media not found")
    file_path = os.path.join(settings.upload_dir, os.path.basename(media.url))
    if os.path.exists(file_path):
        os.remove(file_path)
    db.delete(media)
    db.commit()
    return None
