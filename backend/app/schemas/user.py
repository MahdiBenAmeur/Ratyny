from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class UserBase(BaseModel):
    email: Optional[EmailStr] = None
    phone_number: Optional[str] = None
    display_name: str

class UserCreate(UserBase):
    password: str

class UserLogin(BaseModel):
    username: str # Can be email or phone
    password: str

class User(UserBase):
    id: int
    is_active: bool
    trust_score: float

    class Config:
        from_attributes = True
