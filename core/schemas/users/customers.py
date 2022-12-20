from datetime import date
from datetime import datetime
from typing import Optional

from pydantic import BaseModel
from pydantic import EmailStr

from core.db.models.constants import City
from core.db.models.constants import Gender
from core.db.models.constants import Street
from core.db.models.constants import UserType


class UserBase(BaseModel):
    lbm_user_type: UserType
    lbm_gender: Gender = Gender.HOMME
    lbm_username: Optional[str] = None
    lbm_nickname: Optional[str] = None
    lbm_addr_email: Optional[EmailStr] = None
    lbm_phone_number_one: Optional[str] = None
    lbm_phone_number_two: Optional[str] = None
    lbm_location: City
    lbm_district: Street = Street.COMMERCE
    lbm_password: Optional[str] = None
    lbm_is_active: Optional[bool] = False
    lbm_is_staff: Optional[bool] = False
    lbm_is_superuser: Optional[bool] = False
    created_at: Optional[date] = datetime.now().date()
    modified_at: Optional[date] = datetime.now().date()


class UserCustomerBase(BaseModel):
    lbm_username: str
    lbm_addr_email: EmailStr
    lbm_phone_number_one: str
    lbm_district: Street = Street.COMMERCE


class UserCustomerCreate(UserCustomerBase):
    lbm_password: str


class UserCustomerOut(BaseModel):
    id: int
    lbm_username: str
    lbm_nickname: Optional[str]
    lbm_district: Street

    class Config:
        orm_mode = True


class UserCustomerUpdate(BaseModel):
    lbm_gender: Gender = Gender.HOMME
    lbm_username: Optional[str]
    lbm_addr_email: Optional[EmailStr]
    lbm_nickname: Optional[str]
    lbm_district: Street = Street.COMMERCE
    lbm_phone_number_two: Optional[str]
    modified_at: date = datetime.now().date()

    class Config:
        orm_mode = True
