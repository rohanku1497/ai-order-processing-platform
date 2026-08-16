from fastapi import APIRouter, Depends, HTTPException
import psycopg
from app.schemas.order import OrderCreate,OrderResponse
from app.services.order_service import OrderService
from app.api.dependencies import get_db_connection

router=APIRouter(prefix='/orders',tags=["Orders"])
order_service=OrderService()


@router.post("/",response_model=OrderResponse)
def create_order(
        order: OrderCreate,
        connection : psycopg.Connection=Depends(get_db_connection)
):
    result = order_service.create_order(
    connection,
    order.user_id,
    order.description,
)   
    if result is None:
        raise HTTPException(
            status_code=404,detail="User not found"
        )



    return OrderResponse(
        order_id=result[0],
        user_id=result[1],
        order_date=result[2],
        description=result[3],
        order_status=result[4],
    )

@router.get("/{order_id}", response_model=OrderResponse)
def get_order(
    order_id: int,
    connection: psycopg.Connection = Depends(get_db_connection),
):
    result = order_service.get_order(
        connection,
        order_id,
    )

    if result is None:
        raise HTTPException(
            status_code=404,
            detail="Order not found",
        )

    return OrderResponse(
        order_id=result[0],
        user_id=result[1],
        order_date=result[2],
        description=result[3],
        order_status=result[4],
    )


@router.get("/", response_model=list[OrderResponse])
def list_orders(
    connection: psycopg.Connection = Depends(get_db_connection),
):
    results = order_service.list_orders(connection)

    return [
        OrderResponse(
            order_id=row[0],
            user_id=row[1],
            order_date=row[2],
            description=row[3],
            order_status=row[4],
        )
        for row in results
    ]    