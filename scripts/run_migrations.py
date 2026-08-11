from pathlib import Path
import psycopg

from app.core.config import settings

SQL_DIR=Path(__file__).resolve().parent.parent/'sql'

def run_migrations():
    sql_files=sorted(SQL_DIR.glob("*.sql"))
    if not sql_files:
        print("No SQl migration files found")
        return

    with psycopg.connect(settings.DATABASE_URL) as connection:
        with connection.cursor() as cursor:

            for sql in sql_files:

                sql=sql.read_text(encoding="utf-8")
                cursor.execute(sql)
        connection.commit()

    print("Migrations completed successfully")    

if __name__=="__main__":
    run_migrations()    
