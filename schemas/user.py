from pydantic import BaseModel, EmailStr

class UserBase(BaseModel):
    username : str
    password: str


class User(UserBase):
    id: int
    
    class Config:
        from_attributes = True

class Token(BaseModel):
    access_token: str
    token_type: str
