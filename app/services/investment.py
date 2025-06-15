from typing import Union

from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.charity_project import charity_project_crud
from app.crud.donation import donation_crud
from app.models.charity_project import CharityProject
from app.models.donation import Donation
from app.services.utils import check_and_update_investment_status


async def invest(
    new_obj: Union[CharityProject, Donation],
    session: AsyncSession
) -> Union[CharityProject, Donation]:
    crud = (
        donation_crud if isinstance(new_obj, CharityProject)
        else charity_project_crud
    )
    open_objects = await crud.get_not_fully_invested(session)
    if not open_objects:
        return new_obj
    for obj in open_objects:
        target_need = obj.full_amount - obj.invested_amount
        source_available = new_obj.full_amount - new_obj.invested_amount
        if source_available <= 0:
            break
        invest_amount = min(target_need, source_available)
        obj.invested_amount += invest_amount
        new_obj.invested_amount += invest_amount
        check_and_update_investment_status(obj)
        check_and_update_investment_status(new_obj)
        session.add(obj)
        if new_obj.fully_invested:
            break
    session.add(new_obj)
    await session.commit()
    await session.refresh(new_obj)
    return new_obj
