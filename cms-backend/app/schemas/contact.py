from datetime import datetime
from typing import Optional
from pydantic import BaseModel, ConfigDict, EmailStr


class ContactSubmissionCreate(BaseModel):
    name: str
    email: EmailStr
    phone: str = ""
    subject: str = ""
    message: str


class ContactSubmissionUpdate(BaseModel):
    is_read: Optional[bool] = None


class ContactSubmissionOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str
    email: str
    phone: str
    subject: str
    message: str
    is_read: bool
    created_at: datetime
