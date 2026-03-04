import unittest
import sys
import os
import tempfile
import shutil
import re

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import config
import file_utils

class TestFileUtils(unittest.TestCase):
    def setUp(self):
        self.original_save_path = config.SAVE_PATH
        self.temp_dir = tempfile.mkdtemp()
        config.SAVE_PATH = self.temp_dir
    
    def tearDown(self):
        config.SAVE_PATH = self.original_save_path
        shutil.rmtree(self.temp_dir)
    
    def test_create_log_filename(self):
        filename = file_utils.create_log_filename()
        self.assertTrue(filename.startswith('activity_'))
        self.assertTrue(filename.endswith('.txt'))
        
        pattern = r'activity_\d{8}_\d{6}\.txt'
        self.assertRegex(filename, pattern)
    
    def test_create_log_file(self):
        filepath, filename = file_utils.create_log_file()
        self.assertTrue(os.path.exists(filepath))
        
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            self.assertIn('=== Лог активности ===', content)
            self.assertIn('Старт:', content)
    
    def test_append_final_message(self):
        filepath, _ = file_utils.create_log_file()
        file_utils.append_final_message(filepath)
        
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            self.assertIn('Бот остановлен', content)