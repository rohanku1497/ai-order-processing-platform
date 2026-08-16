from pydantic import BaseModel

class UserCreate(BaseModel):
    username : str
    role : str

class UserResponse(BaseModel):
    user_id : int
    username: str
    role:str    