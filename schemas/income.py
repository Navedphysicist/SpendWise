from pydantic import BaseModel
from datetime import date as dateType
from typing import Optional

class IncomeBase(BaseModel):
    amount: float
    date: dateType
    source: str
    is_recurring: bool = False

class IncomeUpdate(BaseModel):
    amount: Optional[float] = None
    date: Optional[dateType] = None
    source: Optional[str] = None
    is_recurring: Optional[bool] = None

class IncomeDisplay(IncomeBase):
    id: int
    user_id: int

    class Config:
        from_attributes = True
