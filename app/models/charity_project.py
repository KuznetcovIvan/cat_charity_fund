from sqlalchemy import Column, String, Text

from app.core.constants import MAX_LEN_PROJECTNAME
from app.models.base import CharityDonationBase


class CharityProject(CharityDonationBase):
    name = Column(String(MAX_LEN_PROJECTNAME), unique=True, nullable=False)
    description = Column(Text, nullable=False)
