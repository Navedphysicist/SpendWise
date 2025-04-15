from pydantic import BaseModel
from datetime import date

class IncomeBase(BaseModel):
    amount: float
    date: date
    source: str
    is_recurring: bool = False

class IncomeCreate(IncomeBase):
    pass

class IncomeUpdate(IncomeBase):
    amount: float | None = None
    date: date | None = None
    source: str | None = None
    is_recurring: bool | None = None

class Income(IncomeBase):
    id: int
    user_id: int

    class Config:
        from_attributes = True 