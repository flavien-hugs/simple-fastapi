from typing import List

from sqlalchemy.orm import Session

from core.db.models.users import User
from core.db.models.constants import Gender, UserType
from core.schemas.users.cleaners import UserCleanerCreate, UserCleanerUpdate


def create_cleaner_user(user: UserCleanerCreate, db: Session):
    cleaner = User(
        lbm_gender=List[Gender],
        lbm_user_type=UserType.CLEANING,
        lbm_username=user.lbm_username,
        lbm_addr_email=user.lbm_addr_email,
        lbm_district=user.lbm_district,
        lbm_phone_number_one=user.lbm_phone_number_one,
        lbm_phone_number_two=user.lbm_phone_number_two,
        lbm_is_active=True
    )
    db.add(cleaner)
    db.commit()
    db.refresh(cleaner)

    return cleaner


def get_cleaners(db: Session):
    users = db.query(User).filter(User.lbm_is_active, User.lbm_user_type == UserType.CLEANING).all()
    return users


def get_user_cleaner(cleaner_id: int, db: Session):
    return db.query(User).filter(User.id == cleaner_id, User.lbm_user_type == UserType.CLEANING).first()


def get_cleaner_by_district(district: str, db: Session):
    user = db.query(User).filter(User.lbm_district == district).first()
    return user


def update_cleaner_by_id(cleaner_id: int, user: UserCleanerUpdate, db: Session):
    existing_user = db.query(User).filter(User.id == cleaner_id)
    if not existing_user.first():
        return 0
    user.__dict__.update()
    existing_user.update(user.__dict__)
    db.commit()
    return 1


def delete_cleaner_by_id(cleaner_id: int, db: Session):
    existing_user = db.query(User).filter(User.id == cleaner_id)
    if not existing_user.first():
        return 0
    existing_user.delete(synchronize_session=False)
    db.commit()
    return 1
