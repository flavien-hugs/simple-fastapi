from typing import List

from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from fastapi import status
from sqlalchemy.orm import Session

from core.db.repository.users import customers
from core.db.session import get_db
from core.schemas.users.customers import UserCustomerCreate
from core.schemas.users.customers import UserCustomerOut
from core.schemas.users.customers import UserCustomerUpdate

customers_router = APIRouter()


# LIST
# This endpoint returns a list of objects of type `User` serialized using the `User` schema that
# we defined in schemas.users.customers.py. The objects exposed are instances of `db.models.User` that are
# validated and serialized as of the definition of the schema `UserCustomerOut`
@customers_router.get(
    "/", summary="Get all Customers", response_model=List[UserCustomerOut]
)
def get_customers(limit: int = 100, offset: int = 0, db: Session = Depends(get_db)):
    return customers.get_customers(db, offset, limit)


# RETRIEVE
# This endpoint returns a specific `User`, given the value of its `id` field,
# which is passed as a path parameter in the URL. It can also return some
# error condition in case the identifier does not correspond to any object
@customers_router.get(
    "/get/{id}/", summary="Get Customer", response_model=UserCustomerOut
)
def get_customer(id: int, db: Session = Depends(get_db)):
    customer = customers.get_customer(id=id, db=db)
    if not customer:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Customer with this id {id} does not exist",
        )
    return customer


# CREATE
# This endpoint creates a new `User`. The necessary data is read from the request
# body, which is parsed and validated according to the ItemCreate schema defined beforehand
@customers_router.post(
    "/register/", summary="Create Customer", response_model=UserCustomerOut
)
def create_customer(user: UserCustomerCreate, db: Session = Depends(get_db)):
    customer = customers.create_customer(user=user, db=db)
    return customer


# UPDATE
# This endpoint allows to update an existing `User`, identified by its primary key passed as a
# path parameter in the url. The necessary data is read from the request
# body, which is parsed and validated according to the ItemUpdate schema defined beforehand
@customers_router.put(
    "/update/{id}/", summary="Update Customer", response_model=UserCustomerUpdate
)
def update_customer(id: int, user: UserCustomerUpdate, db: Session = Depends(get_db)):
    customer = customers.update_customer(id, user, db)
    if not customer:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Customer with this id {id} does not exist",
        )
    return customer


# DELETE
# This endpoint allows to delete an `User`, identified by its primary key passed as a
# path parameter in the url. It's worth observing that the status code of the response is
# HTTP 204 No Content, since the response body is empty
@customers_router.delete("/delete/{id}/", summary="Delete Customer")
def delete_customer(id: int, db: Session = Depends(get_db)):
    customers.delete_customer(id, db)
    return {"msg": "Customer successfully deleted."}
