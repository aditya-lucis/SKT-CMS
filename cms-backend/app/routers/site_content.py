from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.core.security import get_current_user
from app.models.site_content import SiteContent
from app.schemas.site_content import SiteContentOut, SiteContentUpdate

router = APIRouter(prefix="/api/content", tags=["site-content"])

# Sections manageable through this generic key -> JSON store.
ALLOWED_SECTIONS = {"hero", "about", "site_settings"}


@router.get("/{section}", response_model=SiteContentOut)
def get_section(section: str, db: Session = Depends(get_db)):
    row = db.query(SiteContent).filter(SiteContent.section == section).first()
    if not row:
        return SiteContentOut(section=section, data={})
    return SiteContentOut(section=row.section, data=row.data)


@router.put("/{section}", response_model=SiteContentOut)
def update_section(
    section: str,
    payload: SiteContentUpdate,
    db: Session = Depends(get_db),
    _admin=Depends(get_current_user),
):
    row = db.query(SiteContent).filter(SiteContent.section == section).first()
    if not row:
        row = SiteContent(section=section, data=payload.data)
        db.add(row)
    else:
        row.data = payload.data
    db.commit()
    db.refresh(row)
    return SiteContentOut(section=row.section, data=row.data)
