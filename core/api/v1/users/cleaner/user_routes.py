from typing import List

from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, status

from core.db.session import get_db
from core.schemas.users.cleaners import UserCleanerOut, UserCleanerCreate
from core.db.repository.users.cleaners import create_cleaner_user, get_cleaners, get_user_cleaner

cleaners_router = APIRouter()


@cleaners_router.get("/", summary="Get all cleaners", response_model=List[UserCleanerOut])
def get_households(db: Session = Depends(get_db)):
    households = get_cleaners(db=db)
    return households


@cleaners_router.get("/get/{id}/", summary="Get cleaner", response_model=UserCleanerOut)
def get_cleaner(cleaner_id: int, db: Session = Depends(get_db)):
    cleaner = get_user_cleaner(id=cleaner_id, db=db)
    if not cleaner:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with this id {id} does not exist",
        )
    return cleaner


@cleaners_router.post("/register/", summary="Create cleaner user", response_model=UserCleanerOut)
def create_user(user: UserCleanerCreate, db: Session = Depends(get_db)):
    user = create_cleaner_user(user=user, db=db)
    return user
