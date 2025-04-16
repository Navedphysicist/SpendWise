from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from database import Base


class DbUser(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)

    # Relationships
    incomes = relationship("DbIncome", back_populates="user")
    expenses = relationship("DbExpense", back_populates="user")
