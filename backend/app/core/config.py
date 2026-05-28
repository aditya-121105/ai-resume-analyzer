from pydantic_settings import BaseSettings
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent


class Settings(BaseSettings):
    APP_NAME: str
    DEBUG: bool
    API_V1_STR: str
    DATABASE_URL: str

    class Config:
        env_file = BASE_DIR / ".env"


settings = Settings()