from typing import Type
from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy import func
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.core.security import get_current_user


class ReorderItem(BaseModel):
    id: int
    order_index: int


def build_crud_router(
    *,
    model,
    schema_out: Type[BaseModel],
    schema_create: Type[BaseModel],
    schema_update: Type[BaseModel],
    prefix: str,
    tag: str,
) -> APIRouter:
    """
    Builds a full REST CRUD router (list, get, create, update, delete, reorder)
    for a SQLAlchemy model. Reads are public; writes require a valid admin JWT.
    Used for every repeatable content resource (services, portfolio, team, ...)
    so we don't hand-write ~10 nearly identical routers.
    """
    router = APIRouter(prefix=prefix, tags=[tag])

    @router.get("", response_model=list[schema_out])
    def list_items(db: Session = Depends(get_db)):
        return db.query(model).order_by(model.order_index.asc(), model.id.asc()).all()

    @router.get("/{item_id}", response_model=schema_out)
    def get_item(item_id: int, db: Session = Depends(get_db)):
        obj = db.get(model, item_id)
        if not obj:
            raise HTTPException(status_code=404, detail=f"{tag} not found")
        return obj

    @router.post("", response_model=schema_out, status_code=201)
    def create_item(
        payload: schema_create,
        db: Session = Depends(get_db),
        _admin=Depends(get_current_user),
    ):
        data = payload.model_dump()
        if data.get("order_index") is None:
            max_order = db.query(func.max(model.order_index)).scalar() or 0
            data["order_index"] = max_order + 1
        obj = model(**data)
        db.add(obj)
        db.commit()
        db.refresh(obj)
        return obj

    @router.put("/{item_id}", response_model=schema_out)
    def update_item(
        item_id: int,
        payload: schema_update,
        db: Session = Depends(get_db),
        _admin=Depends(get_current_user),
    ):
        obj = db.get(model, item_id)
        if not obj:
            raise HTTPException(status_code=404, detail=f"{tag} not found")
        for key, value in payload.model_dump(exclude_unset=True).items():
            setattr(obj, key, value)
        db.commit()
        db.refresh(obj)
        return obj

    @router.delete("/{item_id}", status_code=204)
    def delete_item(
        item_id: int,
        db: Session = Depends(get_db),
        _admin=Depends(get_current_user),
    ):
        obj = db.get(model, item_id)
        if not obj:
            raise HTTPException(status_code=404, detail=f"{tag} not found")
        db.delete(obj)
        db.commit()
        return None

    @router.patch("/reorder/bulk", status_code=200)
    def reorder(
        payload: list[ReorderItem],
        db: Session = Depends(get_db),
        _admin=Depends(get_current_user),
    ):
        ids = [item.id for item in payload]
        rows = {row.id: row for row in db.query(model).filter(model.id.in_(ids)).all()}
        for item in payload:
            if item.id in rows:
                rows[item.id].order_index = item.order_index
        db.commit()
        return {"ok": True, "updated": len(rows)}

    return router
