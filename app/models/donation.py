from sqlalchemy import Column, Integer, Text, ForeignKey

from app.models.base import BaseModel


class Donation(BaseModel):
    user_id = Column(
        Integer,
        ForeignKey('user.id'),
        nullable=False,
        name='fk_donation_user_id_user'
    )
    comment = Column(Text, nullable=True)