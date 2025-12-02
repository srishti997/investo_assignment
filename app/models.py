from datetime import datetime
from decimal import Decimal
from pydantic import BaseModel, Field, ConfigDict


# ==========================
# Base OHLCV schema
# ==========================
class OHLCVBase(BaseModel):
    timestamp: datetime = Field(..., alias="datetime", description="Candle timestamp")
    open: float
    high: float
    low: float
    close: float
    volume: int

    # Allow model to accept "datetime" from API input but store internally as "timestamp"
    model_config = ConfigDict(
        populate_by_name=True
    )


# ==========================
# For POST input
# ==========================
class OHLCVCreate(OHLCVBase):
    pass


# ==========================
# For GET output (ORM → Pydantic)
# ==========================
class OHLCVResponse(OHLCVBase):
    model_config = ConfigDict(
        from_attributes=True,      # Pydantic v2 replacement for orm_mode
        populate_by_name=True
    )


# ==========================
# Strategy performance output
# ==========================
class StrategyPerformance(BaseModel):
    short_window: int
    long_window: int
    total_return: float
    num_trades: int
    win_rate: float
