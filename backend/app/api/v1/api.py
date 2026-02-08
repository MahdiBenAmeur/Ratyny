from fastapi import APIRouter
from app.api.v1.endpoints import auth, users, businesses, ratings, incidents

api_router = APIRouter()
api_router.include_router(auth.router, prefix="/auth", tags=["auth"])
api_router.include_router(users.router, prefix="/users", tags=["users"])
api_router.include_router(businesses.router, prefix="/businesses", tags=["businesses"])
api_router.include_router(ratings.router, prefix="/ratings", tags=["ratings"])
api_router.include_router(incidents.router, prefix="/incidents", tags=["incidents"])
