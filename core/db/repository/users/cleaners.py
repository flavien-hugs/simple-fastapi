from sqlalchemy.orm import Session

from core.db.models.constants import UserType
from core.db.models.users import User
from core.schemas.users.cleaners import UserCleanerCreate
from core.schemas.users.cleaners import UserCleanerUpdate


def create_cleaner_user(user: UserCleanerCreate, db: Session):
    cleaner = User(**user.dict())
    cleaner.lbm_user_type = UserType.CLEANER
    cleaner.lbm_is_active = True
    db.add(cleaner)
    db.commit()
    db.refresh(cleaner)

    return cleaner


def get_cleaners(db: Session, skip: int = 0, limit: int = 100):
    users = (
        db.query(User)
        .filter(User.lbm_is_active, User.lbm_user_type == UserType.CLEANER)
        .offset(skip)
        .limit(limit)
        .all()
    )
    return users


def get_cleaner(id: int, db: Session):
    return (
        db.query(User)
        .filter(
            User.id == id, User.lbm_is_active, User.lbm_user_type == UserType.CLEANER
        )
        .first()
    )


def get_cleaner_by_district(district: str, db: Session):
    user = db.query(User).filter(User.lbm_district == district).first()
    return user


def update_cleaner_by_id(id: int, user: UserCleanerUpdate, db: Session):
    existing_user = db.query(User).filter(User.id == id)
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
