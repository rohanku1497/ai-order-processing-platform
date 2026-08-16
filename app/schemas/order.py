from pydantic import BaseModel
from datetime import datetime

class OrderCreate(BaseModel):
    user_id : int
    description : str |None=None

class OrderResponse(BaseModel):
    order_id : int
    user_id :int
    order_date : datetime
    description: str | None
    order_status : str
