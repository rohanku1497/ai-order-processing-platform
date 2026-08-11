import psycopg

from app.core.config import settings


def check_schema():
    with psycopg.connect(settings.DATABASE_URL) as connection:
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT table_name
                FROM information_schema.tables
                WHERE table_schema = 'public'
                ORDER BY table_name;
            """)

            for row in cursor.fetchall():
                print(row[0])


if __name__ == "__main__":
    check_schema()