from datetime import datetime

from sqlalchemy import Integer, DateTime, func
from sqlalchemy.orm import Mapped, mapped_column


class IDMixin:
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)


class OrderMixin:
    order_index: Mapped[int] = mapped_column(Integer, default=0, nullable=False)


class TimestampMixin:
    created_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(
        DateTime, server_default=func.now(), onupdate=func.now()
    )
