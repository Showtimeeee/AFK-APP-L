import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import config

class TestConfig(unittest.TestCase):
    def test_constants_exist(self):
        required_constants = [
            'MAIN_INTERVAL',
            'MICRO_MOVE_INTERVAL',
            'SAVE_PATH',
            'PHRASES',
            'TIME_FORMAT',
            'LOG_HEADER',
            'LOG_FOOTER'
        ]
        
        for const in required_constants:
            self.assertTrue(hasattr(config, const))
    
    def test_intervals_positive(self):
        self.assertGreater(config.MAIN_INTERVAL, 0)
        self.assertGreater(config.MICRO_MOVE_INTERVAL, 0)
        self.assertGreater(config.NOTEPAD_OPEN_DELAY, 0)
    
    def test_save_path_exists(self):
        self.assertTrue(os.path.exists(config.SAVE_PATH))
    
    def test_phrases_not_empty(self):
        self.assertGreater(len(config.PHRASES), 0)
    
    def test_time_format_valid(self):
        from datetime import datetime
        try:
            datetime.now().strftime(config.TIME_FORMAT)
        except:
            self.fail(f"Invalid time format: {config.TIME_FORMAT}")