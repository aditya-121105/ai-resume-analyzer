from fastapi import FastAPI
from sqlalchemy import text

from app.core.config import settings
from app.api.api import api_router
from app.database.database import Base, engine
from app.models.user import User

app = FastAPI(title=settings.APP_NAME)
Base.metadata.create_all(bind=engine)
app.include_router(
    api_router,
    prefix=settings.API_V1_STR
)


@app.get("/")
def root():

    with engine.connect() as connection:
        result = connection.execute(text("SELECT 1"))

    return {
        "message": "API Running",
        "db_test": result.scalar()
    }