from sqlalchemy import Column, Integer, Float, String, Boolean, Date, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Income(Base):
    __tablename__ = "incomes"

    id = Column(Integer, primary_key=True, index=True)
    amount = Column(Float, nullable=False)
    date = Column(Date, nullable=False)
    source = Column(String, nullable=False)
    is_recurring = Column(Boolean, default=False)
    
    # Foreign key
    user_id = Column(Integer, ForeignKey("users.id"))
    
    # Relationship
    user = relationship("User", back_populates="incomes") 