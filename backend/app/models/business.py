from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from app.db.session import Base

class Business(Base):
    __tablename__ = "businesses"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False)
    website_url = Column(String, nullable=True)
    location_address = Column(String, nullable=True)
    is_locked = Column(Boolean, default=True) # Locked immediately after creation per requirements
    
    created_by_id = Column(Integer, ForeignKey("users.id"))
    
    # Relationships will be added here (ratings, posts)
