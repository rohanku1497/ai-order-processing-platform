import psycopg

from app.utils.sql_loader import load_sql
from psycopg.types.json import Json


CREATE_PROCESSED_ORDER_SQL = load_sql(
    "orders/create_processed_orders.sql"
)
GET_PROCESSED_ORDER_SQL = load_sql(
    "orders/get_processed_order.sql"
)

class ProcessedOrderRepository:

    def create_processed_order(
        self,
        connection: psycopg.Connection,
        order_id: int,
        extracted_data: dict,
    ):
        with connection.cursor() as cursor:
            cursor.execute(
                CREATE_PROCESSED_ORDER_SQL,
                (
                    order_id,
                    Json(extracted_data),
                ),
            )

            return cursor.fetchone()

    def get_processed_order(
    self,
    connection: psycopg.Connection,
    order_id: int,
):
        with connection.cursor() as cursor:
            cursor.execute(
            GET_PROCESSED_ORDER_SQL,
            (order_id,),
        )

            return cursor.fetchone()