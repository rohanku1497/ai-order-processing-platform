from app.ai.order_processor import OrderProcessor


class BasicOrderProcessor(OrderProcessor):

    def process(self, order: dict) -> dict:
        return {
            "order_id": order["order_id"],
            "status": "PROCESSED",
        }