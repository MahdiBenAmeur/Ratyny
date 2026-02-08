from typing import Any, List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.api import deps
from app.models.incident import IncidentPost
from app.schemas.incident import IncidentCreate, Incident as IncidentSchema
from app.models.user import User

router = APIRouter()

@router.post("/", response_model=IncidentSchema)
async def create_incident(
    *,
    db: AsyncSession = Depends(deps.get_db),
    incident_in: IncidentCreate,
    current_user: User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Create new incident.
    """
    incident = IncidentPost(
        content=incident_in.content,
        media_urls=incident_in.media_urls,
        business_id=incident_in.business_id,
        user_id=current_user.id
    )
    db.add(incident)
    await db.commit()
    await db.refresh(incident)
    return incident

@router.get("/", response_model=List[IncidentSchema])
async def read_incidents(
    db: AsyncSession = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
) -> Any:
    """
    Retrieve incidents.
    """
    query = select(IncidentPost).where(IncidentPost.is_hidden == False).offset(skip).limit(limit)
    result = await db.execute(query)
    return result.scalars().all()
