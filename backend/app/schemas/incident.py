from pydantic import BaseModel, HttpUrl
from typing import List, Optional

class IncidentBase(BaseModel):
    content: str
    media_urls: Optional[List[str]] = None
    business_id: Optional[int] = None

class IncidentCreate(IncidentBase):
    pass

class Incident(IncidentBase):
    id: int
    user_id: int
    reports_count: int
    is_hidden: bool
    created_at: str

    class Config:
        from_attributes = True
