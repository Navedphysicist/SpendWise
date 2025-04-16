from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from database import get_db
from models.expense import DbExpense
from models.user import DbUser
from schemas.expense import ExpenseBase, ExpenseUpdate, ExpenseDisplay
from dependencies import get_current_user

router = APIRouter(prefix="/expenses", tags=["expenses"])


@router.post("", response_model=ExpenseDisplay)
def create_expense(
    expense: ExpenseBase,
    db: Session = Depends(get_db),
    current_user: DbUser = Depends(get_current_user)
):
    db_expense = DbExpense(**expense.model_dump(), user_id=current_user.id)
    db.add(db_expense)
    db.commit()
    db.refresh(db_expense)
    return db_expense


@router.get("", response_model=List[ExpenseDisplay])
def get_expenses(
    db: Session = Depends(get_db),
    current_user: DbUser = Depends(get_current_user)
):
    return db.query(DbExpense).filter(DbExpense.user_id == current_user.id).all()


@router.get("/total-expense", response_model=dict)
def get_total_expenses(
    db: Session = Depends(get_db),
    current_user: DbUser = Depends(get_current_user)
):
    expenses = db.query(DbExpense).filter(
        DbExpense.user_id == current_user.id).all()
    total = sum(expense.amount for expense in expenses)
    return {
        'total-expense': total
    }


@router.patch("/{category}", response_model=List[ExpenseDisplay])
def update_expenses_by_category(
    category: str,
    expense_update: ExpenseUpdate,
    db: Session = Depends(get_db),
    current_user: DbUser = Depends(get_current_user)
):
    expenses = db.query(DbExpense).filter(
        DbExpense.category == category,
        DbExpense.user_id == current_user.id
    ).all()
    if not expenses:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"No expenses found for category: {category}"
        )

    for expense in expenses:
        if expense_update.amount is not None:
            expense.amount = expense_update.amount
        if expense_update.date is not None:
            expense.date = expense_update.date
        if expense_update.is_recurring is not None:
            expense.is_recurring = expense_update.is_recurring
        if expense_update.category is not None:
            expense.category = expense_update.category

    db.commit()
    for expense in expenses:
        db.refresh(expense)
    return expenses


@router.delete("/{category}", status_code=status.HTTP_204_NO_CONTENT)
def delete_expenses_by_category(
    category: str,
    db: Session = Depends(get_db),
    current_user: DbUser = Depends(get_current_user)
):
    expenses = db.query(DbExpense).filter(
        DbExpense.category == category,
        DbExpense.user_id == current_user.id
    ).all()
    if not expenses:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"No expenses found for category: {category}"
        )

    for expense in expenses:
        db.delete(expense)
    db.commit()
    return None
