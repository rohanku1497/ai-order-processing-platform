import psycopg
from app.db.database import get_connection
from app.repositories.order_repository import OrderRepository
from app.repositories.user_repository import UserRepository

class OrderService:
    def __init__(self):
        self.repository=OrderRepository()
        self.user_repository=UserRepository()

    def create_order(
            self,
            connection : psycopg.Connection,
            user_id:int,
            description: str | None,
    ):
        user= self.user_repository.get_user(
            connection,
            user_id,
        )
        
        if user is None:
            return None
        try:

        
            result=self.repository.create_order(
                connection,
                user_id,
                description)
            connection.commit()
            return result
        
        except Exception:
            connection.rollback()
            raise

            
        

    def get_order(
        self,
        connection: psycopg.Connection,
        order_id: int,
    ):
        return self.repository.get_order(
            connection,
            order_id,
        )

    def list_orders(
        self,
        connection: psycopg.Connection,
    ):
        return self.repository.list_orders(connection)

