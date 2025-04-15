from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from database import get_db
from models.income import Income
from models.user import User
from schemas.income import IncomeCreate, IncomeUpdate, Income as IncomeSchema
from dependencies import get_current_user
from sqlalchemy import func

router = APIRouter(prefix="/incomes", tags=["incomes"])

@router.post("", response_model=IncomeSchema)
def create_income(
    income: IncomeCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    db_income = Income(**income.model_dump(), user_id=current_user.id)
    db.add(db_income)
    db.commit()
    db.refresh(db_income)
    return db_income

@router.get("", response_model=List[IncomeSchema])
def get_incomes(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return db.query(Income).filter(Income.user_id == current_user.id).all()

@router.get("/{income_id}", response_model=IncomeSchema)
def get_income(
    income_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    income = db.query(Income).filter(
        Income.id == income_id,
        Income.user_id == current_user.id
    ).first()
    if not income:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Income not found"
        )
    return income

@router.patch("/{income_id}", response_model=IncomeSchema)
def update_income(
    income_id: int,
    income_update: IncomeUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    db_income = db.query(Income).filter(
        Income.id == income_id,
        Income.user_id == current_user.id
    ).first()
    if not db_income:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Income not found"
        )
    
    update_data = income_update.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_income, key, value)
    
    db.commit()
    db.refresh(db_income)
    return db_income

@router.delete("/{income_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_income(
    income_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    db_income = db.query(Income).filter(
        Income.id == income_id,
        Income.user_id == current_user.id
    ).first()
    if not db_income:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Income not found"
        )
    
    db.delete(db_income)
    db.commit()
    return None

@router.get("/total/amount", response_model=float)
def get_total_income(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    total = db.query(Income).filter(Income.user_id == current_user.id).with_entities(
        func.sum(Income.amount)
    ).scalar()
    return total or 0.0 