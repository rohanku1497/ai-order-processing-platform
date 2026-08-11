import psycopg
from app.core.config import settings

def get_connection():
    return psycopg.connect(
        settings.DATABASE_URL
    )


