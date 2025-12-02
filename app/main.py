from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from .db import get_db, Base, engine
from . import crud
from .models import OHLCVCreate, OHLCVResponse, StrategyPerformance
from .strategy import moving_average_crossover

Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/data", response_model=list[OHLCVResponse])
def get_data(db: Session = Depends(get_db)):
    return crud.get_all_ohlcv(db)

@app.post("/data", response_model=list[OHLCVResponse])
def add_data(payload: list[OHLCVCreate], db: Session = Depends(get_db)):
    if not payload:
        raise HTTPException(status_code=400, detail="Payload cannot be empty")
    return crud.create_many_ohlcv(db, payload)

@app.get("/strategy/performance", response_model=StrategyPerformance)
def strategy(short_window: int = 20, long_window: int = 50, db: Session = Depends(get_db)):
    rows = crud.get_all_ohlcv(db)
    result = moving_average_crossover(rows, short_window, long_window)
    return StrategyPerformance(**result)
