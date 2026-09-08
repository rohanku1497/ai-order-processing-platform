import psycopg

from app.utils.sql_loader import load_sql

CREATE_ORDER_SQL= load_sql("orders/create_order.sql")
GET_ORDER_SQL = load_sql("orders/get_order.sql")
LIST_ORDERS_SQL = load_sql("orders/list_orders.sql")
UPDATE_STATUS_SQL = load_sql("orders/update_status.sql")

class OrderRepository:

    def create_order(
        self,
        connection: psycopg.Connection,
        user_id: int,
        description: str | None,
    ):
        with connection.cursor() as cursor:
            cursor.execute(
                CREATE_ORDER_SQL,
                (user_id, description),
            )

            return cursor.fetchone()

    def get_order(
        self,
        connection: psycopg.Connection,
        order_id: int,
    ):
        with connection.cursor() as cursor:
            cursor.execute(
                GET_ORDER_SQL,
                (order_id,),
            )

            return cursor.fetchone()

    def list_orders(
        self,
        connection: psycopg.Connection,
    ):
        with connection.cursor() as cursor:
            cursor.execute(LIST_ORDERS_SQL)

            return cursor.fetchall()

    def update_status(
    self,
    connection: psycopg.Connection,
    order_id: int,
    status: str,
):
        with connection.cursor() as cursor:
            cursor.execute(
                UPDATE_STATUS_SQL,
                (status, order_id),
            )

