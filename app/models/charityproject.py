from sqlalchemy import Column, String, Text

from app.models.base import BaseModel
from app.core.constants import MAX_LEN_PROJECTNAME


class CharityProject(BaseModel):
    name = Column(String(MAX_LEN_PROJECTNAME), unique=True, nullable=False)
    description = Column(Text, nullable=False)