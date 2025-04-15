from pydantic import BaseModel
from datetime import date

class ExpenseBase(BaseModel):
    amount: float
    date: date
    category: str
    is_recurring: bool = False

class ExpenseCreate(ExpenseBase):
    pass

class ExpenseUpdate(ExpenseBase):
    amount: float | None = None
    date: date | None = None
    category: str | None = None
    is_recurring: bool | None = None

class Expense(ExpenseBase):
    id: int
    user_id: int

    class Config:
        from_attributes = True 