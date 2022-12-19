from sqlalchemy.orm import Session

from core.db.models.users import User
from core.config.hashing import Hasher
from core.db.models.constants import UserType
from core.schemas.users.customers import UserCustomerCreate, UserCustomerUpdate


def create_customer_user(user: UserCustomerCreate, db: Session):
    user = User(
        lbm_user_type=UserType.CUSTOMER,
        lbm_username=user.lbm_username,
        lbm_addr_email=user.lbm_addr_email,
        lbm_phone_number_one=user.lbm_phone_number_one,
        lbm_district=user.lbm_district,
        lbm_password=Hasher.get_password_hash(user.lbm_password),
        lbm_is_active=True
    )
    db.add(user)
    db.commit()
    db.refresh(user)

    return user


def get_users_customers(db: Session):
    users = db.query(User).filter(User.lbm_is_active, User.lbm_user_type == UserType.CUSTOMER).all()
    return users


def get_user_customer(customer_id: int, db: Session):
    return db.query(User).filter(User.id == customer_id, User.lbm_user_type == UserType.CUSTOMER).first()


def get_user_by_district(district: str, db: Session):
    user = db.query(User).filter(User.lbm_district == district).first()
    return user


def update_user_by_id(customer_id: int, user: UserCustomerUpdate, db: Session):
    existing_user = db.query(User).filter(User.id == customer_id)
    if not existing_user.first():
        return 0
    user.__dict__.update()
    existing_user.update(user.__dict__)
    db.commit()
    return 1


def delete_user_by_id(customer_id: int, db: Session):
    existing_user = db.query(User).filter(User.id == customer_id)
    if not existing_user.first():
        return 0
    existing_user.delete(synchronize_session=False)
    db.commit()
    return 1
