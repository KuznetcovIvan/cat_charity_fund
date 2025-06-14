from datetime import datetime as dt
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Union
from app.models.charity_project import CharityProject
from app.models.donation import Donation
from app.crud.charity_project import charity_project_crud
from app.crud.donation import donation_crud


async def invest(
    new_object: Union[CharityProject, Donation],
    session: AsyncSession
) -> Union[CharityProject, Donation]:
    is_project = isinstance(new_object, CharityProject)
    crud = charity_project_crud if is_project else donation_crud
    open_objects = await crud.get_not_fully_invested(session)
    available_amount = new_object.full_amount - new_object.invested_amount
    for obj in open_objects:
        to_invest = min(
            obj.full_amount - obj.invested_amount, available_amount
        )
        obj.invested_amount += to_invest
        new_object.invested_amount += to_invest
        available_amount -= to_invest
        if obj.invested_amount == obj.full_amount:
            obj.fully_invested = True
            obj.close_date = dt.now()
        if available_amount == 0:
            break
    if new_object.invested_amount == new_object.full_amount:
        new_object.fully_invested = True
        new_object.close_date = dt.now()
    await session.commit()
    await session.refresh(new_object)
    return new_object