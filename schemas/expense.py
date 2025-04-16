from pydantic import BaseModel
from datetime import date as dateType
from typing import Optional

class ExpenseBase(BaseModel):
    amount: float
    date: dateType
    category: str
    is_recurring: bool = False


class ExpenseUpdate(BaseModel):
    amount: Optional[float] = None
    date: Optional[dateType] = None
    category: Optional[str] = None
    is_recurring: Optional[bool] = None

class ExpenseDisplay(ExpenseBase):
    id: int
    user_id: int

    class Config:
        from_attributes = True 