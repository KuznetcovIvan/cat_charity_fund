from datetime import datetime as dt
from typing import Union

from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.charity_project import charity_project_crud
from app.crud.donation import donation_crud
from app.models.charity_project import CharityProject
from app.models.donation import Donation


async def invest(
    new_object: Union[CharityProject, Donation],
    session: AsyncSession
) -> Union[CharityProject, Donation]:
    crud = (
        donation_crud if isinstance(new_object, CharityProject)
        else charity_project_crud
    )
    open_objects = await crud.get_not_fully_invested(session)
    if not open_objects:
        return new_object
    for object in open_objects:
        target_need = object.full_amount - object.invested_amount
        source_available = new_object.full_amount - new_object.invested_amount
        if source_available <= 0:
            break
        invest_amount = min(target_need, source_available)
        object.invested_amount += invest_amount
        new_object.invested_amount += invest_amount
        if object.invested_amount == object.full_amount:
            object.fully_invested = True
            object.close_date = dt.now()
        if new_object.invested_amount == new_object.full_amount:
            new_object.fully_invested = True
            new_object.close_date = dt.now()
            session.add(object)
            break
        session.add(object)
    session.add(new_object)
    await session.commit()
    await session.refresh(new_object)
    return new_object
