import random
from datetime import datetime
import config


class ActivityGenerator:
    def __init__(self):
        self.line_counter = 0
        self.actions_done = 0
    
    def generate_line(self):
        self.line_counter += 1
        self.actions_done += 1
        
        timestamp = datetime.now().strftime(config.TIME_FORMAT)
        phrase = random.choice(config.PHRASES)
        text = f"{self.line_counter:3d}. [{timestamp}] {phrase}"
        
        return text, timestamp, phrase
    
    def get_stats(self):
        """Возвращает статистику"""
        return self.line_counter, self.actions_done

        
