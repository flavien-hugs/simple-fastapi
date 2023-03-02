from typing import List

from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from fastapi import status
from sqlalchemy.orm import Session

from core.db.repository.users.cleaners import create_cleaner_user
from core.db.repository.users.cleaners import get_cleaner
from core.db.repository.users.cleaners import get_cleaner_by_district
from core.db.repository.users.cleaners import get_cleaners
from core.db.session import get_db
from core.schemas.users.cleaners import UserCleanerCreate
from core.schemas.users.cleaners import UserCleanerOut

from core.db.models.users import User
from core.api.v1.users.route_login import get_current_user

route_cleaners = APIRouter()


@route_cleaners.get(
    "/", summary="Get all cleaners", response_model=List[UserCleanerOut]
)
def get_all_cleaners(limit: int = 100, offset: int = 0, db: Session = Depends(get_db)):
    households = get_cleaners(db, offset, limit)
    return households


@route_cleaners.get(
    "/get/{district}/",
    summary="Get cleaner by district",
    response_model=List[UserCleanerOut],
)
def get_cleaner_by_district(
    district: str,
    db: Session = Depends(get_db),
):
    cleaner = get_cleaner_by_district(district=district, db=db)
    if not cleaner:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with this district {district} does not exist",
        )
    return cleaner


@route_cleaners.get("/get/{id}/", summary="Get cleaner", response_model=UserCleanerOut)
def get_cleaner_id(id: int, db: Session = Depends(get_db)):
    cleaner = get_cleaner(id, db)
    if not cleaner:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with this id {id} does not exist",
        )
    return cleaner


@route_cleaners.post(
    "/register/", summary="Create cleaner user", response_model=UserCleanerOut
)
def create_cleaner(user: UserCleanerCreate, db: Session = Depends(get_db)):
    user = create_cleaner_user(user=user, db=db)
    return user
