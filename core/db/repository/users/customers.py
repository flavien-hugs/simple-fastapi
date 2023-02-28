from sqlalchemy.orm import Session

from core.config.hashing import Hasher
from core.db.models.constants import UserType
from core.db.models.users import User
from core.schemas.users.customers import UserCustomerCreate
from core.schemas.users.customers import UserCustomerUpdate


def create_customer(user: UserCustomerCreate, db: Session):
    user = User(**user.dict())
    user.lbm_user_type = UserType.CUSTOMER
    user.lbm_password = Hasher.get_password_hash(user.lbm_password)
    user.lbm_is_active = True
    db.add(user)
    db.commit()
    db.refresh(user)

    return user


def get_customers(db: Session, skip: int = 0, limit: int = 50):
    users = (
        db.query(User)
        .filter(User.lbm_is_active, User.lbm_user_type == UserType.CUSTOMER)
        .offset(skip)
        .limit(limit)
        .all()
    )
    return users


def get_customer(id: int, db: Session):
    return (
        db.query(User)
        .filter(
            User.id == id, User.lbm_is_active, User.lbm_user_type == UserType.CUSTOMER
        )
        .first()
    )


def update_customer_by_id(id: int, user: UserCustomerUpdate, db: Session):
    existing_customer = db.query(User).filter(
        User.id == id, User.lbm_user_type == UserType.CUSTOMER
    )
    if not existing_customer.first():
        return 0
    user.__dict__.update(id=id)
    existing_customer.update(user.__dict__)
    db.commit()
    return 1


def delete_customer_by_id(id: int, db: Session):
    existing_customer = db.query(User).filter(
        User.id == id, User.lbm_user_type == UserType.CUSTOMER
    )
    if not existing_customer.first():
        return 0
    existing_customer.delete(synchronize_session=False)
    db.commit()
    return 1


def get_customer_by_email(email: str, db: Session):
    user = db.query(User).filter(User.lbm_addr_email == email).first()
    return user
