import os
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")

    # Database
    database_url: str = "mysql+pymysql://nexus_user:nexus_pass_dev@localhost:3306/nexus_cms"

    # Auth
    secret_key: str = "change-this-secret-key-in-production"
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 60 * 24 * 7  # 7 days

    # Seeded single-admin account (created on first startup if no admin exists)
    admin_username: str = "admin"
    admin_password: str = "admin123"

    # CORS - comma separated origins allowed to hit this API
    cors_origins: str = "http://localhost:5173,http://localhost:5174,http://127.0.0.1:5173,http://127.0.0.1:5174"

    # File uploads
    upload_dir: str = "app/uploads"
    max_upload_mb: int = 8

    # Public base URL of this API (used to build absolute media URLs)
    api_base_url: str = "http://localhost:8000"

    @property
    def cors_origins_list(self) -> list[str]:
        return [o.strip() for o in self.cors_origins.split(",") if o.strip()]


settings = Settings()
os.makedirs(settings.upload_dir, exist_ok=True)
