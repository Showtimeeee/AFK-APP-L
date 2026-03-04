import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import config
from activity_generator import ActivityGenerator

class TestActivityGenerator(unittest.TestCase):
    def setUp(self):
        self.generator = ActivityGenerator()
    
    def test_initial_counters(self):
        self.assertEqual(self.generator.line_counter, 0)
        self.assertEqual(self.generator.actions_done, 0)
    
    def test_generate_line(self):
        text, timestamp, phrase = self.generator.generate_line()
        
        self.assertEqual(self.generator.line_counter, 1)
        self.assertEqual(self.generator.actions_done, 1)
        
        expected_start = f"{1:3d}. [{timestamp}]"
        self.assertTrue(text.startswith(expected_start))
        self.assertIn(phrase, config.PHRASES)
    
    def test_multiple_generations(self):
        for i in range(5):
            self.generator.generate_line()
        
        self.assertEqual(self.generator.line_counter, 5)
        self.assertEqual(self.generator.actions_done, 5)
    
    def test_get_stats(self):
        self.generator.generate_line()
        self.generator.generate_line()
        
        lines, actions = self.generator.get_stats()
        self.assertEqual(lines, 2)
        self.assertEqual(actions, 2)
    
    def test_phrase_from_list(self):
        generated_phrases = set()
        for _ in range(20):
            _, _, phrase = self.generator.generate_line()
            generated_phrases.add(phrase)
        
        for phrase in generated_phrases:
            self.assertIn(phrase, config.PHRASES)