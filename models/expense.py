from sqlalchemy import Column, Integer, Float, String, Boolean, Date, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Expense(Base):
    __tablename__ = "expenses"

    id = Column(Integer, primary_key=True, index=True)
    amount = Column(Float, nullable=False)
    date = Column(Date, nullable=False)
    category = Column(String, nullable=False)
    is_recurring = Column(Boolean, default=False)
    
    # Foreign key
    user_id = Column(Integer, ForeignKey("users.id"))
    
    # Relationship
    user = relationship("User", back_populates="expenses") 