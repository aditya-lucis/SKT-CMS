from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from app.core.config import settings
from app.core.database import engine, Base, SessionLocal
from app.core.security import hash_password
import app.models  # noqa: F401 - ensures every model is registered on Base.metadata

from app.models.admin_user import AdminUser
from app.routers import auth, site_content, media, contact
from app.routers.resources import all_resource_routers
from app.routers.public import router as public_router


def ensure_admin_seeded():
    """Create the single admin account from .env if it doesn't exist yet."""
    db = SessionLocal()
    try:
        exists = db.query(AdminUser).filter(AdminUser.username == settings.admin_username).first()
        if not exists:
            db.add(AdminUser(
                username=settings.admin_username,
                hashed_password=hash_password(settings.admin_password),
            ))
            db.commit()
            print(f"[seed] Created admin user '{settings.admin_username}'")
    finally:
        db.close()


@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(bind=engine)
    ensure_admin_seeded()
    yield


app = FastAPI(title="SKT CMS API", version="1.0.0", lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins_list,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/uploads", StaticFiles(directory=settings.upload_dir), name="uploads")

app.include_router(auth.router)
app.include_router(site_content.router)
app.include_router(media.router)
app.include_router(contact.router)
app.include_router(contact.public_router)
app.include_router(public_router)
for r in all_resource_routers:
    app.include_router(r)


@app.get("/api/health")
def health():
    return {"status": "ok"}
