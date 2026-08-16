import os


BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__)
        )
    )
)

SQL_DIR = os.path.join(BASE_DIR, "sql", "queries")


def load_sql(path: str) -> str:
    sql_file = os.path.join(SQL_DIR, path)

    with open(sql_file, "r", encoding="utf-8") as file:
        return file.read()