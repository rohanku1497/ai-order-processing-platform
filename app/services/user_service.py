import psycopg

from app.repositories.user_repository import UserRepository

class UserService:
    def __init__(self):
        self.repository=UserRepository()

    def create_user(
            self,
            connection : psycopg.Connection,
            username : str,
            role : str
    ) :
        return self.repository.create_user(
            connection,
            username,
            role
        )

    def get_user(self,
                    connection : psycopg.Connection,
        user_id : int,
        role : str,):
        return self. repository,create_user(
            connection,
            user_id,
            role
        )

    def list_users(
    self,
    connection: psycopg.Connection,
):
        return self.repository.list_users(connection)
    

        
        