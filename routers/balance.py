from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy import func
from database import get_db
from models.income import Income
from models.expense import Expense
from models.user import User
from dependencies import get_current_user

router = APIRouter(prefix="/balance", tags=["balance"])

@router.get("/total", response_model=float)
def get_total_balance(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    # Get total income
    total_income = db.query(Income).filter(Income.user_id == current_user.id).with_entities(
        func.sum(Income.amount)
    ).scalar() or 0.0
    
    # Get total expenses
    total_expenses = db.query(Expense).filter(Expense.user_id == current_user.id).with_entities(
        func.sum(Expense.amount)
    ).scalar() or 0.0
    
    # Calculate balance
    balance = total_income - total_expenses
    return balance 