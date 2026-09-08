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

class OrderItem(BaseModel):
    name:str
    quantity:int
    size : str | None = None

class ProcessOrder(BaseModel):
    items : list[OrderItem]
    delivery_address : str |None =None

class ProcessedOrderResponse(BaseModel):
    processed_order_id : int
    order_id :int
    extracted_data : dict
    created_at : datetime