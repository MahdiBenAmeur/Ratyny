from typing import Any, List, Optional
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, or_

from app.api import deps
from app.models.business import Business
from app.schemas.business import BusinessCreate, Business as BusinessSchema
from app.models.user import User

router = APIRouter()

@router.get("/", response_model=List[BusinessSchema])
async def read_businesses(
    db: AsyncSession = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    search: Optional[str] = None
) -> Any:
    """
    Retrieve businesses.
    """
    query = select(Business)
    
    if search:
        query = query.where(
            or_(
                Business.name.ilike(f"%{search}%"),
                Business.website_url.ilike(f"%{search}%")
            )
        )
        
    query = query.offset(skip).limit(limit)
    result = await db.execute(query)
    return result.scalars().all()

@router.post("/", response_model=BusinessSchema)
async def create_business(
    *,
    db: AsyncSession = Depends(deps.get_db),
    business_in: BusinessCreate,
    current_user: User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Create new business.
    """
    # Check if business with same name/url already exists (optional robust check)
    
    business = Business(
        name=business_in.name,
        website_url=business_in.website_url,
        location_address=business_in.location_address,
        created_by_id=current_user.id,
        is_locked=True # Locked by default as per requirements
    )
    db.add(business)
    await db.commit()
    await db.refresh(business)
    return business

@router.get("/{business_id}", response_model=BusinessSchema)
async def read_business(
    business_id: int,
    db: AsyncSession = Depends(deps.get_db),
) -> Any:
    """
    Get business by ID.
    """
    result = await db.execute(select(Business).where(Business.id == business_id))
    business = result.scalars().first()
    if not business:
        raise HTTPException(status_code=404, detail="Business not found")
    return business
