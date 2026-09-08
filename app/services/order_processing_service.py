import psycopg

from app.repositories.order_repository import OrderRepository
from app.repositories.processed_order_repository import ProcessedOrderRepository
from app.ai.openai_order_processor import OpenAIOrderProcessor


class OrderProcessingService:

    def __init__(self):
        self.order_repository = OrderRepository()
        self.processed_order_repository = ProcessedOrderRepository()
        self.processor = OpenAIOrderProcessor()

    def process_order(
        self,
        connection: psycopg.Connection,
        order_id: int,
    ):
        # Get order
        order = self.order_repository.get_order(
            connection,
            order_id,
        )

        if order is None:
            return None

        if order[4]=="COMPLETED":
            return None

        if order[4] == "FAILED":
            self.order_repository.update_status(
            connection,
            order_id,
            "PROCESSING",
    )
        connection.commit()


        # PENDING -> PROCESSING
        self.order_repository.update_status(
            connection,
            order_id,
            "PROCESSING",
        )

        connection.commit()

        # Convert DB row to dictionary
        order_data = {
            "order_id": order[0],
            "user_id": order[1],
            "order_date": order[2],
            "description": order[3],
            "order_status": "PROCESSING",
        }

        try:
            # Send order to OpenAI
            result = self.processor.process(order_data)

            # Save OpenAI result
            self.processed_order_repository.create_processed_order(
                connection,
                order_id,
                result,
            )

            # PROCESSING -> COMPLETED
            self.order_repository.update_status(
                connection,
                order_id,
                "COMPLETED",
            )

            connection.commit()

            return result

        except Exception:
            connection.rollback()

            self.order_repository.update_status(
                connection,
                order_id,
                "FAILED",
            )

            connection.commit()

            raise

    def get_processed_order(
    self,
    connection: psycopg.Connection,
    order_id: int,
):
        return self.processed_order_repository.get_processed_order(
        connection,
        order_id,
    )