from fastapi import APIRouter, Depends,HTTPException
import psycopg


from app.api.dependencies import get_db_connection
from app.schemas.user import UserCreate, UserResponse
from app.services.user_service import UserService


router = APIRouter(prefix="/users", tags=["Users"])

user_service = UserService()



@router.post("/", response_model=UserResponse)
def create_user(
    user: UserCreate,
    connection: psycopg.Connection = Depends(get_db_connection),
):
    result = user_service.create_user(
        connection,
        user.username,
        user.role,
    )

    connection.commit()

    return UserResponse(
        user_id=result[0],
        username=result[1],
        role=result[2],
    )

@router.get("/{user_id}", response_model=UserResponse)
def get_user(
    user_id: int,
    connection: psycopg.Connection = Depends(get_db_connection),
):
    result = user_service.get_user(
        connection,
        user_id,
    )

    if result is None:
        raise HTTPException(status_code=404, detail="User not found")

    return UserResponse(
        user_id=result[0],
        username=result[1],
        role=result[2],
    )


@router.get("/", response_model=list[UserResponse])
def list_users(
    connection: psycopg.Connection = Depends(get_db_connection),
):
    results = user_service.list_users(connection)

    return [
        UserResponse(
            user_id=row[0],
            username=row[1],
            role=row[2],
        )
        for row in results
    ]