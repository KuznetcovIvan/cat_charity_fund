from datetime import datetime as dt
from typing import Optional

from pydantic import BaseModel, PositiveInt, Field
from app.core.constants import MIN_STR_LENGTH


class DonationBase(BaseModel):
    full_amount: PositiveInt
    comment: Optional[str] = Field(None, min_length=MIN_STR_LENGTH)


class DonationCreate(DonationBase):
    pass


class DonationDBShort(DonationBase):
    id: int
    create_date: dt

    class Config:
        orm_mode = True


class DonationDB(DonationDBShort):
    user_id: int
    invested_amount: int
    fully_invested: bool
    close_date: Optional[dt]

    class Config:
        orm_mode = True
