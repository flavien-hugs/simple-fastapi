from typing import List

from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, status

from core.db.session import get_db
from core.schemas.users.customers import UserCustomerOut, UserCustomerCreate
from core.db.repository.users.customers import create_customer_user, get_user_customer, get_users_customers

customers_router = APIRouter()


@customers_router.get("/", summary="Get all Customers", response_model=List[UserCustomerOut])
def get_customers(db: Session = Depends(get_db)):
    customers = get_users_customers(db=db)
    return customers


@customers_router.get("/get/{id}/", summary="Get customer", response_model=UserCustomerOut)
def get_customer(customer_id: int, db: Session = Depends(get_db)):
    customer = get_user_customer(id=customer_id, db=db)
    if not customer:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with this id {id} does not exist",
        )
    return customer


@customers_router.post("/register/", summary="Create customer user ", response_model=UserCustomerOut)
def create_user(user: UserCustomerCreate, db: Session = Depends(get_db)):
    user = create_customer_user(user=user, db=db)
    return user
