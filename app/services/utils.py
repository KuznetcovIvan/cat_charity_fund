from datetime import datetime as dt
from typing import Union

from app.models.charity_project import CharityProject
from app.models.donation import Donation


def check_and_update_investment_status(
    obj: Union[CharityProject, Donation]
) -> None:
    if obj.invested_amount == obj.full_amount:
        obj.fully_invested = True
        obj.close_date = dt.now()
