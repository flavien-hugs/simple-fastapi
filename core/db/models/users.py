from sqlalchemy import Boolean
from sqlalchemy import Column
from sqlalchemy import Enum
from sqlalchemy import String

from core.db.base_class import Base
from core.db.models.constants import City
from core.db.models.constants import Gender
from core.db.models.constants import Street
from core.db.models.constants import UserType
from core.db.models.mixins import BaseModel


class User(BaseModel, Base):

    __tablename__ = "users"

    lbm_user_type = Column(Enum(UserType), default=UserType.CUSTOMER)
    lbm_gender = Column(Enum(Gender), default=Gender.HOMME)
    lbm_username = Column(String(180), nullable=False)
    lbm_nickname = Column(String(180), unique=True, nullable=True)
    lbm_location = Column(Enum(City), default=City.BOUAKE)
    lbm_district = Column(Enum(Street), default=Street.COMMERCE)
    lbm_addr_email = Column(String(80), nullable=True, unique=True)
    lbm_phone_number_one = Column(String(15), nullable=False, unique=True)
    lbm_phone_number_two = Column(String(15), nullable=True, unique=True)
    lbm_password = Column(String(100), nullable=True)
    lbm_is_active = Column(Boolean(), default=False)
    lbm_is_staff = Column(Boolean(), default=False)
    lbm_is_superuser = Column(Boolean(), default=False)

    def __str__(self):
        return f"{self.lbm_username}, {self.lbm_phone_number_one}"
