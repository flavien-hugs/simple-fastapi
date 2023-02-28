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

from core.db.models.users import User
from core.api.v1.users.route_login import get_current_user_from_token

route_users = APIRouter()


# CREATE
# This endpoint creates a new `User`. The necessary data is read from the request
# body, which is parsed and validated according to the ItemCreate schema defined beforehand
@route_users.post(
    "/register/",
    summary="Create Customer",
    response_model=UserCustomerOut
)
def create_customer(
    user: UserCustomerCreate,
    db: Session = Depends(get_db),
):
    customer = customers.create_customer(user=user, db=db)
    return customer


# LIST
# This endpoint returns a list of objects of type `User` serialized using the `User` schema that
# we defined in schemas.users.customers.py. The objects exposed are instances of `db.models.User` that are
# validated and serialized as of the definition of the schema `UserCustomerOut`
@route_users.get(
    "/all/",
    summary="Get all Customers",
    response_model=List[UserCustomerOut]
)
def get_all_customers(limit: int = 50, offset: int = 0, db: Session = Depends(get_db)):
    all_customers = customers.get_customers(db, offset, limit)
    return all_customers


# READ
# This endpoint returns a specific `User`, given the value of its `id` field,
# which is passed as a path parameter in the URL. It can also return some
# error condition in case the identifier does not correspond to any object
@route_users.get(
    "/get/{id}/",
    summary="Get Customer",
    response_model=UserCustomerOut
)
def read_customer(
    id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user_from_token),
):
    id = current_user.id
    customer = customers.get_customer(id, db)
    if not customer:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Customer with this id {user_id} does not exist",
        )
    return customer


# UPDATE
# This endpoint allows to update an existing `User`, identified by its primary key passed as a
# path parameter in the url. The necessary data is read from the request
# body, which is parsed and validated according to the ItemUpdate schema defined beforehand
@route_users.put(
    "/update/{id}/",
    summary="Update Customer",
    response_model=UserCustomerUpdate
)
def update_customer(
    id: int,
    user: UserCustomerUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user_from_token),
):
    current_user_id = current_user.id
    customer_retrieved = customers.update_customer(id, user, db)
    if not customer_retrieved:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Customer with this id {id} does not exist",
        )
    if customer_retrieved.id == current_user.id or current_user.lbm_is_superuser:
        customers.update_customer_by_id(id=current_user_id, user=user, db=db)
    else:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="You are not authorized to update.",
        )
    return customer


# DELETE
# This endpoint allows to delete an `User`, identified by its primary key passed as a
# path parameter in the url. It's worth observing that the status code of the response is
# HTTP 204 No Content, since the response body is empty
@route_users.delete(
    "/delete/{id}/",
    summary="Delete Customer"
)
def delete_customer(
    id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user_from_token)
):

    current_user_id = current_user.id
    customer = customers.delete_customer(id, db)
    if not customer:
        return HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Customer with {id} does not exist",
        )

    if customer.id == current_user.id or current_user.is_superuser:
        customers.delete_customer_by_id(id=current_user_id, db=db)
        return {"msg": "User successfully deleted."}

    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="You are not permitted !"
    )
