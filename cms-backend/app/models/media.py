from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from app.core.database import Base
from app.models.base import IDMixin, TimestampMixin


class Media(Base, IDMixin, TimestampMixin):
    __tablename__ = "media"

    filename: Mapped[str] = mapped_column(String(255), nullable=False)
    url: Mapped[str] = mapped_column(String(500), nullable=False)
    alt: Mapped[str] = mapped_column(String(255), default="", nullable=False)
