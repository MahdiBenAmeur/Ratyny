from typing import Any, List
from fastapi import APIRouter, Body, Depends, HTTPException
from fastapi.encoders import jsonable_encoder
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.api import deps
from app.core import security
from app.models.user import User
from app.schemas.user import UserCreate, User as UserSchema

router = APIRouter()

@router.post("/", response_model=UserSchema)
async def create_user(
    *,
    db: AsyncSession = Depends(deps.get_db),
    user_in: UserCreate,
) -> Any:
    """
    Create new user.
    """
    # Check existing user
    stmt = select(User).where(
        (User.email == user_in.email) | (User.phone_number == user_in.phone_number)
    )
    result = await db.execute(stmt)
    user = result.scalars().first()
    
    if user:
        raise HTTPException(
            status_code=400,
            detail="The user with this username already exists in the system.",
        )
        
    user = User(
        email=user_in.email,
        phone_number=user_in.phone_number,
        display_name=user_in.display_name,
        hashed_password=security.get_password_hash(user_in.password),
        is_active=True,
    )
    db.add(user)
    await db.commit()
    await db.refresh(user)
    return user

@router.get("/me", response_model=UserSchema)
async def read_user_me(
    current_user: User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Get current user.
    """
    return current_user
