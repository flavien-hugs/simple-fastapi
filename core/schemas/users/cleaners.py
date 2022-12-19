from typing import Optional, List
from datetime import date, datetime

from pydantic import BaseModel, EmailStr

from core.db.models.constants import UserType, Gender


class UserBase(BaseModel):
    lbm_user_type: UserType
    lbm_gender: Gender
    lbm_username: Optional[str] = None
    lbm_nickname: Optional[str] = None
    lbm_addr_email: Optional[EmailStr] = None
    lbm_phone_number_one: Optional[str] = None
    lbm_phone_number_two: Optional[str] = None
    lbm_location: Optional[str] = None
    lbm_district: Optional[str] = None
    lbm_password: Optional[str] = None
    lbm_is_active: Optional[bool] = False
    lbm_is_staff: Optional[bool] = False
    lbm_is_superuser: Optional[bool] = False
    created_at: Optional[date] = datetime.now().date()
    modified_at: Optional[date] = datetime.now().date()


class UserCleanerBase(BaseModel):
    lbm_gender: Gender
    lbm_addr_email: Optional[str] = EmailStr
    lbm_username: str
    lbm_nickname: str
    lbm_district: str
    lbm_phone_number_one: str
    lbm_phone_number_two: Optional[str]


class UserCleanerCreate(UserCleanerBase):
    pass


class UserCleanerOut(BaseModel):
    lbm_nickname: str
    lbm_district: str

    class Config:
        orm_mode = True


class UserCleanerUpdate(UserCleanerBase):
    lbm_gender: Gender
    lbm_username: Optional[str]
    lbm_nickname: Optional[str]
    lbm_district: Optional[str]
    lbm_phone_number_one: Optional[str]
    lbm_phone_number_two: Optional[str]
    modified_at: Optional[date] = datetime.now().date()

    class Config:
        orm_mode = True
