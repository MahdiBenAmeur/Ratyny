from typing import Any, List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.api import deps
from app.models.rating import Rating
from app.schemas.rating import RatingCreate, Rating as RatingSchema
from app.models.user import User

router = APIRouter()

@router.post("/", response_model=RatingSchema)
async def create_rating(
    *,
    db: AsyncSession = Depends(deps.get_db),
    rating_in: RatingCreate,
    current_user: User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Create new rating.
    """
    # Check if user already rated this business
    existing_rating = await db.execute(
        select(Rating).where(
            (Rating.user_id == current_user.id) & 
            (Rating.business_id == rating_in.business_id)
        )
    )
    if existing_rating.scalars().first():
        raise HTTPException(status_code=400, detail="User already rated this business")

    rating = Rating(
        user_id=current_user.id,
        business_id=rating_in.business_id,
        score=rating_in.score,
        comment=rating_in.comment,
        proof_url=rating_in.proof_url
    )
    db.add(rating)
    await db.commit()
    await db.refresh(rating)
    return rating

@router.get("/business/{business_id}", response_model=List[RatingSchema])
async def read_business_ratings(
    business_id: int,
    db: AsyncSession = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
) -> Any:
    """
    Retrieve ratings for a business.
    """
    query = select(Rating).where(Rating.business_id == business_id).offset(skip).limit(limit)
    result = await db.execute(query)
    return result.scalars().all()
