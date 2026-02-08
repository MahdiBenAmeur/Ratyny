from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.db.session import Base

class Rating(Base):
    __tablename__ = "ratings"

    id = Column(Integer, primary_key=True, index=True)
    score = Column(Integer, nullable=False) # 1-5
    comment = Column(String, nullable=True)
    proof_url = Column(String, nullable=True)
    
    user_id = Column(Integer, ForeignKey("users.id"))
    business_id = Column(Integer, ForeignKey("businesses.id"))
    
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    # Relationships
    # user = relationship("User", back_populates="ratings")
    # business = relationship("Business", back_populates="ratings")
