import pyautogui
import time
import sys
import threading
from datetime import datetime

import config
import file_utils
import notepad_controller
from activity_generator import ActivityGenerator


# Флаг для остановки бота
running = True

def wait_for_enter():
    """Ждет нажатия Enter для остановки"""
    global running
    try:
        input()
    except:
        pass
    running = False

def print_header():
    """Печатает заголовок при запуске"""
    print("="*50)
    print(config.TEXT_STARTUP)
    print("="*50)
    print(f"📁 Файлы сохраняются в: {config.SAVE_PATH}")
    print("🟢 Бот запущен")
    print(f"⏏️  {config.TEXT_STOP_INSTRUCTION}")
    print("="*50)

def print_footer(stats, filename):
    """Печатает завершающую информацию"""
    print("\n" + "="*50)
    print(config.TEXT_STOP)
    print(config.TEXT_FILE_SAVED.format(filename=filename))
    print(f"📍 Путь: {config.PROJECT_PATH}")
    print(config.TEXT_LINES_COUNT.format(count=stats[0]))
    print("="*50)

def wait_with_micro_movements(seconds):
    """Ожидание с микро-движениями мыши и проверкой флага"""
    global running
    
    for i in range(seconds):
        if not running:
            return False
        if i % config.MICRO_MOVE_INTERVAL == 0 and i > 0:
            notepad_controller.micro_movement()
        time.sleep(1)
    
    return True

# ========== ОСНОВНАЯ ПРОГРАММА ==========

if __name__ == "__main__":
    try:
        # Инициализация
        print_header()
        
        # Создание файла в корне проекта
        filepath, filename = file_utils.create_log_file()
        
        # Открытие блокнота
        notepad_controller.open_notepad(filepath)
        notepad_controller.maximize_notepad()
        notepad_controller.go_to_end_and_newline()
        
        print(config.TEXT_READY)
        print("="*50)
        
        # Запускаем поток для ожидания Enter
        enter_thread = threading.Thread(target=wait_for_enter, daemon=True)
        enter_thread.start()
        
        # Генератор активности
        generator = ActivityGenerator()
        
        # Основной цикл
        while running:
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
            if not wait_with_micro_movements(config.MAIN_INTERVAL):
                break
        
        # Завершение работы
        print("\n⏳ Завершение работы...")
        notepad_controller.write_line(
            config.LOG_FOOTER.format(
                timestamp=datetime.now().strftime(config.TIME_FORMAT)
            )
        )
        notepad_controller.save_file()
        time.sleep(1)
        
        stats = generator.get_stats()
        print_footer(stats, filename)
        
    except Exception as e:
        print(f"❌ Ошибка: {e}")
    finally:
        sys.exit(0)
