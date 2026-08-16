import psycopg

from app.core.config import settings
from app.repositories.user_repository import UserRepository


def main():
    repository = UserRepository()

    with psycopg.connect(settings.DATABASE_URL) as connection:

        user = repository.create_user(
            connection,
            "test_user",
            "customer",
        )

        connection.commit()

        print("Created:", user)

        user_id = user[0]

        result = repository.get_user(
            connection,
            user_id,
        )

        print("Retrieved:", result)

        users = repository.list_users(connection)

        print("All users:")
        for user in users:
            print(user)


if __name__ == "__main__":
    main()