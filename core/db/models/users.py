from sqlalchemy import Column, Boolean, String, Enum

from .mixins import BaseModel
from .constants import Gender, UserType, City

from ..base_class import Base


class User(BaseModel, Base):

    __tablename__ = "users"

    lbm_user_type = Column(Enum(UserType), default=UserType.CUSTOMER)
    lbm_gender = Column(Enum(Gender), default=Gender.MAN)
    lbm_username = Column(String(80), unique=True, nullable=False)
    lbm_nickname = Column(String(80), unique=True, nullable=True)
    lbm_location = Column(Enum(City), default=City.BKE)
    lbm_district = Column(String(80), nullable=True)
    lbm_addr_email = Column(String(80), nullable=False, unique=True)
    lbm_phone_number_one = Column(String(15), nullable=False, unique=True)
    lbm_phone_number_two = Column(String(15), nullable=True, unique=True)
    lbm_password = Column(String(100), nullable=False)
    lbm_is_active = Column(Boolean(), default=False)
    lbm_is_staff = Column(Boolean(), default=False)
    lbm_is_superuser = Column(Boolean(), default=False)

    def __str__(self):
        return f"{self.lbm_username}, {self.lbm_phone_number_one}"
