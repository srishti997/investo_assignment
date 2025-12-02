import pandas as pd
from sqlalchemy.orm import Session
from app.db import SessionLocal
from app.orm_models import OHLCV

FILE_PATH = "HINDALCO_1D.xlsx"

def load_data():
    df = pd.read_excel(FILE_PATH)

    # Make column names lowercase
    df.columns = [c.lower().strip() for c in df.columns]

    db: Session = SessionLocal()

    for _, row in df.iterrows():
        db.add(OHLCV(
            datetime = pd.to_datetime(row["datetime"]),
            open = float(row["open"]),
            high = float(row["high"]),
            low = float(row["low"]),
            close = float(row["close"]),
            volume = int(row["volume"])
        ))

    db.commit()
    db.close()
    print("Data loaded successfully!")

if __name__ == "__main__":
    load_data()
