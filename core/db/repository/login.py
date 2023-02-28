from sqlalchemy.orm import Session

from core.db.models.users import User


def get_user(username: str, db: Session):
    user = db.query(User).filter(User.lbm_addr_email == username).first()
    return user
