from datetime import datetime
from pydantic import BaseModel, ConfigDict


class MediaOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    filename: str
    url: str
    alt: str
    created_at: datetime
