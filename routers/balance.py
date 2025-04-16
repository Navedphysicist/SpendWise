from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from models.income import DbIncome
from models.expense import DbExpense
from models.user import DbUser
from dependencies import get_current_user

router = APIRouter(prefix="/balance", tags=["balance"])


@router.get("/", response_model=dict)
def get_total_balance(
    db: Session = Depends(get_db),
    current_user: DbUser = Depends(get_current_user)
):
    # Get total income
    incomes = db.query(DbIncome).filter(DbIncome.user_id == current_user.id).all()
    total_income = sum(income.amount for income in incomes)

    # Get total expenses
    expenses = db.query(DbExpense).filter(DbExpense.user_id == current_user.id).all()
    total_expense = sum(expense.amount for expense in expenses)

    # Calculate balance
    balance = total_income- total_expense
    return {
        "balance" : balance
    }
