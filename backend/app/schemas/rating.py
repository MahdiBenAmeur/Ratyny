from pydantic import BaseModel, Field
from typing import Optional

class RatingBase(BaseModel):
    score: int = Field(..., ge=1, le=5)
    comment: Optional[str] = None
    proof_url: Optional[str] = None

class RatingCreate(RatingBase):
    business_id: int

class RatingUpdate(RatingBase):
    pass

class Rating(RatingBase):
    id: int
    user_id: int
    business_id: int
    created_at: str # ISO format handled by pydantic automatically often, but explicit string is safer for response
    updated_at: Optional[str] = None

    class Config:
        from_attributes = True
