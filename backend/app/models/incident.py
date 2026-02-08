from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, DateTime
from sqlalchemy.dialects.postgresql import ARRAY # Postgres specific
from sqlalchemy.sql import func
from app.db.session import Base

class IncidentPost(Base):
    __tablename__ = "incident_posts"

    id = Column(Integer, primary_key=True, index=True)
    content = Column(String, nullable=False)
    media_urls = Column(ARRAY(String), nullable=True) # Array of URLs
    
    user_id = Column(Integer, ForeignKey("users.id"))
    business_id = Column(Integer, ForeignKey("businesses.id"), nullable=True)
    
    reports_count = Column(Integer, default=0)
    is_hidden = Column(Boolean, default=False)
    
    created_at = Column(DateTime(timezone=True), server_default=func.now())
