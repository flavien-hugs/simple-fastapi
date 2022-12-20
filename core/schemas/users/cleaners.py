from datetime import date
from datetime import datetime
from typing import List
from typing import Optional

from pydantic import BaseModel
from pydantic import EmailStr

from core.db.models.constants import City
from core.db.models.constants import Gender
from core.db.models.constants import Street
from core.db.models.constants import UserType


class UserBase(BaseModel):
    lbm_user_type: UserType
    lbm_gender: List[Gender]
    lbm_username: Optional[str] = None
    lbm_nickname: Optional[str] = None
    lbm_addr_email: Optional[EmailStr] = None
    lbm_phone_number_one: Optional[str] = None
    lbm_phone_number_two: Optional[str] = None
    lbm_location: List[City]
    lbm_district: List[Street]
    lbm_password: Optional[str] = None
    lbm_is_active: Optional[bool] = False
    lbm_is_staff: Optional[bool] = False
    lbm_is_superuser: Optional[bool] = False
    created_at: Optional[date] = datetime.now().date()
    modified_at: Optional[date] = datetime.now().date()


class UserCleaner(BaseModel):
    lbm_gender: Gender = Gender.HOMME
    lbm_addr_email: Optional[str] = EmailStr
    lbm_username: str
    lbm_nickname: str
    lbm_district: Street = Street.COMMERCE
    lbm_phone_number_one: str
    lbm_phone_number_two: Optional[str]


class UserCleanerCreate(BaseModel):
    lbm_gender: Gender = Gender.HOMME
    lbm_username: str
    lbm_nickname: str
    lbm_district: Street = Street.COMMERCE
    lbm_phone_number_one: str
    lbm_phone_number_two: Optional[str] = None


class UserCleanerOut(BaseModel):
    id: int
    lbm_nickname: str
    lbm_district: Street

    class Config:
        orm_mode = True


class UserCleanerUpdate(BaseModel):
    lbm_gender: Gender = Gender.HOMME
    lbm_addr_email: Optional[EmailStr] = None
    lbm_username: Optional[str] = None
    lbm_nickname: Optional[str] = None
    lbm_district: Street = Street.COMMERCE
    lbm_phone_number_one: Optional[str] = None
    lbm_phone_number_two: Optional[str] = None
    modified_at: Optional[date] = datetime.now().date()
