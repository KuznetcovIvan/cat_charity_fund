from typing import Optional

from pydantic import BaseModel, Field, PositiveInt, validator

from app.core.constants import MAX_LEN_PROJECTNAME, MIN_STR_LENGTH
from app.schemas.base import CharityDonationBase, CharityDonationDBBase


class CharityProjectBase(BaseModel):
    name: Optional[str] = Field(
        None, min_length=MIN_STR_LENGTH, max_length=MAX_LEN_PROJECTNAME
    )
    description: Optional[str] = Field(None, min_length=MIN_STR_LENGTH)


class CharityProjectCreate(CharityProjectBase, CharityDonationBase):
    name: str = Field(
        ..., min_length=MIN_STR_LENGTH, max_length=MAX_LEN_PROJECTNAME
    )
    description: str = Field(..., min_length=MIN_STR_LENGTH)
    full_amount: PositiveInt


class CharityProjectUpdate(CharityProjectBase):
    full_amount: Optional[PositiveInt]

    @validator('name', 'description', 'full_amount')
    def check_not_none(cls, value):
        if value is None:
            raise ValueError('Поле не может быть пустым!')
        return value


class CharityProjectDB(CharityProjectBase, CharityDonationDBBase):
    id: int
