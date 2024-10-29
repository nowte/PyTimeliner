# test_timeliner.py

import unittest
from datetime import datetime, timedelta
from pytimeliner import TimeLiner

class TestTimeLiner(unittest.TestCase):
    
    def setUp(self):
        self.timeliner = TimeLiner()
        self.test_date = datetime(2023, 1, 1, 12, 0, 0)
    
    def test_format_time(self):
        formatted_time = self.timeliner.format_time(self.test_date)
        self.assertEqual(formatted_time, "2023-01-01 12:00:00")
    
    def test_time_since(self):
        past = datetime.now() - timedelta(days=2)
        time_since = self.timeliner.time_since(past)
        self.assertIn("days ago", time_since)
    
    def test_add_time(self):
        result = self.timeliner.add_time(self.test_date, days=1, hours=2)
        expected = self.test_date + timedelta(days=1, hours=2)
        self.assertEqual(result, expected)
    
    def test_subtract_time(self):
        result = self.timeliner.subtract_time(self.test_date, days=1, hours=2)
        expected = self.test_date - timedelta(days=1, hours=2)
        self.assertEqual(result, expected)

    def test_get_date_range(self):
        start = datetime(2023, 1, 1)
        end = datetime(2023, 1, 5)
        dates = self.timeliner.get_date_range(start, end)
        self.assertEqual(len(dates), 5)
        self.assertEqual(dates[0], start)
        self.assertEqual(dates[-1], end)
    
    def test_translate_time_info(self):
        self.timeliner.set_language("es")
        translated_text = self.timeliner.translate_time_info("2 days ago")
        self.assertNotEqual(translated_text, "2 days ago")
        self.assertIsInstance(translated_text, str)

if __name__ == "__main__":
    unittest.main()
