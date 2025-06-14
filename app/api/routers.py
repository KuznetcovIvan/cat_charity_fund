from fastapi import APIRouter

from app.api.endpoints.charity_project import router as charityproject_router
from app.api.endpoints.donation import router as donation_router
from app.api.endpoints.user import router as user_router

main_router = APIRouter()
main_router.include_router(
    charityproject_router,
    prefix='/charity_project',
    tags=['charity_projects']
)
main_router.include_router(
    donation_router,
    prefix='/donation',
    tags=['donations']
)
main_router.include_router(user_router)
