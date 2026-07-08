from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.core.security import get_current_user
from app.models.contact import ContactSubmission
from app.schemas.contact import ContactSubmissionCreate, ContactSubmissionOut, ContactSubmissionUpdate

router = APIRouter(prefix="/api/contact-submissions", tags=["contact"])
public_router = APIRouter(prefix="/api/contact", tags=["contact"])


@public_router.post("", response_model=ContactSubmissionOut, status_code=201)
def submit_contact(payload: ContactSubmissionCreate, db: Session = Depends(get_db)):
    submission = ContactSubmission(**payload.model_dump())
    db.add(submission)
    db.commit()
    db.refresh(submission)
    return submission


@router.get("", response_model=list[ContactSubmissionOut])
def list_submissions(db: Session = Depends(get_db), _admin=Depends(get_current_user)):
    return db.query(ContactSubmission).order_by(ContactSubmission.created_at.desc()).all()


@router.patch("/{submission_id}", response_model=ContactSubmissionOut)
def update_submission(
    submission_id: int,
    payload: ContactSubmissionUpdate,
    db: Session = Depends(get_db),
    _admin=Depends(get_current_user),
):
    obj = db.get(ContactSubmission, submission_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Submission not found")
    for key, value in payload.model_dump(exclude_unset=True).items():
        setattr(obj, key, value)
    db.commit()
    db.refresh(obj)
    return obj


@router.delete("/{submission_id}", status_code=204)
def delete_submission(submission_id: int, db: Session = Depends(get_db), _admin=Depends(get_current_user)):
    obj = db.get(ContactSubmission, submission_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Submission not found")
    db.delete(obj)
    db.commit()
    return None
