from fastapi import FastAPI
from app.core.config import settings
from app.api.health import router
from app.api.users import router as users_router

app=FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION
)

app.include_router(router)
app.include_router(users_router)