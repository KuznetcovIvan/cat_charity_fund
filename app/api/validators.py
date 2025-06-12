from http import HTTPStatus

from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.charity_project import charity_project_crud


async def check_name_duplicate(
    project_name: str,
    session: AsyncSession
) -> None:
    if await charity_project_crud.get_by_attribute(
        'name', project_name, session
    ) is not None:
        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST,
            detail='Проект с таким именем уже существует!'
        )