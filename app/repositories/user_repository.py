import psycopg

from app.utils.sql_loader import load_sql


CREATE_USER_SQL = load_sql("users/create_user.sql")
GET_USER_SQL = load_sql("users/get_user.sql")
LIST_USERS_SQL = load_sql("users/list_users.sql")

class UserRepository:

    def create_user(
            self,
            connection:psycopg.Connection,
            username:str,
            role:str
    ):
        with connection.cursor() as cursor:
            cursor.execute(CREATE_USER_SQL,(username,role),)

            return cursor.fetchone()

    def get_user(
            self,
            conneection: psycopg.Connection,
            user_id:int
    ):
        with conneection.cursor() as cursor:
            cursor.execute(GET_USER_SQL,(user_id,),)

            return cursor.fetchone()

    def list_users(self, connection : psycopg.Connection):
        with connection.cursor() as cursor:
            cursor.execute(LIST_USERS_SQL)

            return cursor.fetchall()