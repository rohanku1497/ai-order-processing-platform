from app.ai.openai_client import client
from app.ai.order_processor import OrderProcessor
from app.schemas.order import ProcessOrder


class OpenAIOrderProcessor(OrderProcessor):

    def process(self, order: dict) -> dict:

        response = client.responses.parse(
            model="gpt-4o-mini",
            input=[
                {
                    "role": "system",
                    "content": (
                        "Extract all order information from the customer's order description. "
                        "Extract every item, its quantity and size if provided. "
                        "If a delivery address is present, extract the complete address exactly. "
                        "Never omit an address that appears in the description. "
                        "If no address is present, use null."
                    ),
                },
                {
                    "role": "user",
                    "content": order["description"],
                },
            ],
            text_format=ProcessOrder,
        )

        processed_order = response.output_parsed

        return processed_order.model_dump()