from datetime import datetime as dt

from sqlalchemy import Boolean, Column, DateTime, Integer, CheckConstraint

from app.core.db import Base

FULL_AMOUNT_POSITIVE = 'огр_сумма_положительная'
INVESTED_AMOUNT_POSITIVE = 'огр_инвестировано_не_отрицательно'
INVESTED_LESS_OR_EQUAL_FULL = 'огр_инвестировано_не_больше_суммы'
INVESTMENT_STATUS_MATCH = 'огр_валидность_завершения'


class CharityDonationBase(Base):
    __abstract__ = True

    full_amount = Column(Integer, nullable=False)
    invested_amount = Column(Integer, default=0)
    fully_invested = Column(Boolean, default=False)
    create_date = Column(DateTime, default=dt.now)
    close_date = Column(DateTime, nullable=True)

    __table_args__ = (
        CheckConstraint(
            'full_amount > 0',
            name='amount_must_be_positive'
        ),
        CheckConstraint(
            'invested_amount >= 0',
            name='invested_amount_cannot_be_negative'
        ),
        CheckConstraint(
            'invested_amount <= full_amount',
            name='invested_amount_not_greater_than_full_amount'
        ),
        CheckConstraint(
            '(fully_invested IS TRUE AND close_date IS NOT NULL) OR '
            '(fully_invested IS FALSE AND close_date IS NULL)',
            name='investment_status_and_close_date_consistency'
        )
    )

    def __repr__(self):
        return (
            f'{self.__class__.__name__}('
            f'id={self.id}, '
            f'full_amount={self.full_amount}, '
            f'invested_amount={self.invested_amount}, '
            f'fully_invested={self.fully_invested}, '
            f'create_date=\'{self.create_date}\', '
            f'close_date=\'{self.close_date}\')'
        )
