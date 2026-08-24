import psycopg

from app.core.config import settings
from app.repositories.order_repository import OrderRepository


def main():
    repository = OrderRepository()

    with psycopg.connect(settings.DATABASE_URL) as connection:

        order = repository.create_order(
            connection,
            user_id=13,
            description="Test order",
        )

        connection.commit()

        print("Created:", order)

        order_id = order[0]

        result = repository.get_order(
            connection,
            order_id,
        )

        print("Retrieved:", result)

        orders = repository.list_orders(connection)

        print("All orders:")
        for order in orders:
            print(order)


if __name__ == "__main__":
    main()