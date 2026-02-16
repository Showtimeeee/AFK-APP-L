# bot.py - основной файл бота
import pyautogui
import time
import sys
from datetime import datetime

import config
import file_utils
import notepad_controller
from activity_generator import ActivityGenerator

def print_header():
    """Печатает заголовок при запуске"""
    print("="*50)
    print(config.TEXT_STARTUP)
    print("="*50)

def print_footer(stats, filename):
    """Печатает завершающую информацию"""
    print("\n" + "="*50)
    print(config.TEXT_STOP)
    print(config.TEXT_FILE_SAVED.format(filename=filename))
    print(config.TEXT_LINES_COUNT.format(count=stats[0]))
    print("="*50)

def wait_with_micro_movements(seconds):
    """Ожидание с микро-движениями мыши"""
    print(config.TEXT_NEXT_ACTION.format(seconds=seconds))
    
    for i in range(seconds):
        if i % config.MICRO_MOVE_INTERVAL == 0:
            notepad_controller.micro_movement()
        time.sleep(1)

# ========== ОСНОВНАЯ ПРОГРАММА ==========

if __name__ == "__main__":
    try:
        # Инициализация
        print_header()
        
        # Создание файла
        filepath, filename = file_utils.create_log_file()
        
        # Открытие блокнота
        notepad_controller.open_notepad(filepath)
        notepad_controller.maximize_notepad()
        notepad_controller.go_to_end_and_newline()
        
        print(config.TEXT_READY)
        print(config.TEXT_STOP_INSTRUCTION)
        print("="*50)
        
        # Генератор активности
        generator = ActivityGenerator()
        
        # Основной цикл
        while True:
            # Генерируем и печатаем строку
            text, timestamp, phrase = generator.generate_line()
            notepad_controller.write_line(text)
            notepad_controller.save_file()
            
            print(config.TEXT_LINE_WRITTEN.format(
                num=generator.line_counter,
                timestamp=timestamp,
                phrase=phrase
            ))
            
            # Ожидание с микро-движениями
            wait_with_micro_movements(config.MAIN_INTERVAL)
            
    except KeyboardInterrupt:
        # Завершение работы
        notepad_controller.write_line(
            config.LOG_FOOTER.format(
                timestamp=datetime.now().strftime(config.TIME_FORMAT)
            )
        )
        notepad_controller.save_file()
        
        stats = generator.get_stats()
        print_footer(stats, filename)
        
        sys.exit(0)
        