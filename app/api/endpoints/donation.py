from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from crud.donation import donation_crud
from app.core.db import get_async_session
from app.core.user import current_superuser
from app.schemas.donation import DonationDB

router = APIRouter()


@router.get(
    '/',
    response_model=list[DonationDB],
    response_model_exclude_none=True,
    dependencies=[Depends(current_superuser)]
)
async def get_all_donations(
    session: AsyncSession = Depends(get_async_session)
):
    return await donation_crud.get_multi(session)