from typing import Any
from pydantic import BaseModel


class SiteContentOut(BaseModel):
    section: str
    data: dict[str, Any]


class SiteContentUpdate(BaseModel):
    data: dict[str, Any]
