import os
from datetime import datetime
import config

def create_log_filename():
    """Создает имя файла лога с текущей датой и временем"""
    timestamp = datetime.now().strftime(config.FILENAME_FORMAT.replace("activity_", ""))
    return f"activity_{timestamp}"

def create_log_file():
    """Создает файл лога и возвращает путь к нему"""
    filename = create_log_filename()
    filepath = os.path.join(config.SAVE_PATH, filename)
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(config.LOG_HEADER)
        f.write(f"Старт: {datetime.now().strftime(config.TIMESTAMP_FORMAT)}\n")
        f.write(config.LOG_SEPARATOR)
    
    return filepath, filename

def append_final_message(filepath):
    """Добавляет финальное сообщение в файл лога"""
    with open(filepath, "a", encoding="utf-8") as f:
        f.write(config.LOG_FOOTER.format(
            timestamp=datetime.now().strftime(config.TIMESTAMP_FORMAT)
        ))
