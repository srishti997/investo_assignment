import unittest
from pydantic import ValidationError
from app.models import OHLCVCreate


class TestValidation(unittest.TestCase):

    def test_valid_input(self):
        item = OHLCVCreate(
            datetime="2024-01-01T10:00:00",
            open=100.5,
            high=110.2,
            low=99.1,
            close=105.2,
            volume=1500000
        )
        self.assertEqual(float(item.open), 100.5)

    def test_invalid_volume(self):
        with self.assertRaises(ValidationError):
            OHLCVCreate(
                datetime="2024-01-01T10:00:00",
                open=100.5,
                high=110.2,
                low=99.1,
                close=105.2,
                volume="bad"
            )

    def test_missing_field(self):
        with self.assertRaises(ValidationError):
            OHLCVCreate(
                datetime="2024-01-01T10:00:00",
                open=100.5,
                high=110.2,
                low=99.1,
                # missing close
                volume=1000
            )


if __name__ == "__main__":
    unittest.main()
