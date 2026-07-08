from sqlalchemy import String, JSON
from sqlalchemy.orm import Mapped, mapped_column

from app.core.database import Base
from app.models.base import IDMixin, TimestampMixin


class SiteContent(Base, IDMixin, TimestampMixin):
    """
    Generic key -> JSON blob store for singleton sections that don't need
    their own table (hero, about, site_settings). Keeps the schema flexible
    without needing a migration every time a new field is added to a section.
    """
    __tablename__ = "site_content"

    section: Mapped[str] = mapped_column(String(60), unique=True, index=True, nullable=False)
    data: Mapped[dict] = mapped_column(JSON, nullable=False, default=dict)
