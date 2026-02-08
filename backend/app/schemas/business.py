from pydantic import BaseModel, HttpUrl
from typing import Optional, List

class BusinessBase(BaseModel):
    name: str
    website_url: Optional[str] = None
    location_address: Optional[str] = None

class BusinessCreate(BusinessBase):
    pass

class Business(BusinessBase):
    id: int
    is_locked: bool
    created_by_id: int

    class Config:
        from_attributes = True
