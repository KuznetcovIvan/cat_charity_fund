from sqlalchemy import Column, ForeignKey, Integer, Text

from app.models.base import CharityDonationBase


class Donation(CharityDonationBase):
    user_id = Column(
        Integer,
        ForeignKey('user.id'),
        nullable=False,
        name='fk_donation_user_id_user'
    )
    comment = Column(Text, nullable=True)
