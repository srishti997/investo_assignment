from typing import List
import pandas as pd
from .orm_models import OHLCV

def moving_average_crossover(rows: List[OHLCV], short_window=20, long_window=50):
    if len(rows) < long_window:
        return {
            "short_window": short_window,
            "long_window": long_window,
            "total_return": 0,
            "num_trades": 0,
            "win_rate": 0
        }

    df = pd.DataFrame({
        "datetime": [r.datetime for r in rows],
        "close": [float(r.close) for r in rows]
    }).sort_values("datetime")

    df["short_ma"] = df["close"].rolling(short_window).mean()
    df["long_ma"] = df["close"].rolling(long_window).mean()

    df["signal"] = (df["short_ma"] > df["long_ma"]).astype(int)
    df["position_change"] = df["signal"].diff().fillna(0)
    df["return"] = df["close"].pct_change().fillna(0)
    df["strategy_return"] = df["signal"].shift(1).fillna(0) * df["return"]

    total_return = (1 + df["strategy_return"]).prod() - 1
    num_trades = df[df["position_change"] != 0].shape[0]

    return {
        "short_window": short_window,
        "long_window": long_window,
        "total_return": float(total_return),
        "num_trades": int(num_trades),
        "win_rate": 0  # simplified
    }
