from typing import List
from sqlalchemy.orm import Session
from .orm_models import OHLCV
from .models import OHLCVCreate


def get_all_ohlcv(db: Session) -> List[OHLCV]:
    return db.query(OHLCV).order_by(OHLCV.datetime).all()

def create_many_ohlcv(db: Session, data_list: List[OHLCVCreate]):
    objs = [
        OHLCV(
            datetime=d.datetime,
            open=d.open,
            high=d.high,
            low=d.low,
            close=d.close,
            volume=d.volume
        )
        for d in data_list
    ]
    db.add_all(objs)
    db.commit()
    return objs
