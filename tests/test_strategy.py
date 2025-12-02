import unittest
from app.strategy import moving_average_crossover
from app.orm_models import OHLCV


class Dummy:
    """Simple dummy record for testing strategy."""
    def __init__(self, dt, close):
        self.datetime = dt
        self.close = close


class TestStrategy(unittest.TestCase):

    def test_strategy_no_data(self):
        rows = []
        result = moving_average_crossover(rows, 5, 20)
        self.assertEqual(result["total_return"], 0)

    def test_strategy_small_data(self):
        rows = [
            Dummy("2024-01-01", 100),
            Dummy("2024-01-02", 102),
            Dummy("2024-01-03", 104),
            Dummy("2024-01-04", 106),
            Dummy("2024-01-05", 108),
        ]

        result = moving_average_crossover(rows, 2, 3)
        self.assertIn("total_return", result)
        self.assertIn("num_trades", result)


if __name__ == "__main__":
    unittest.main()
