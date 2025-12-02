from sqlalchemy import Column, DateTime, Numeric, BigInteger
from .db import Base

class OHLCV(Base):
    __tablename__ = "ohlcv"

    datetime = Column(DateTime(timezone=True), primary_key=True)
    open = Column(Numeric(12,4), nullable=False)
    high = Column(Numeric(12,4), nullable=False)
    low = Column(Numeric(12,4), nullable=False)
    close = Column(Numeric(12,4), nullable=False)
    volume = Column(BigInteger, nullable=False)
