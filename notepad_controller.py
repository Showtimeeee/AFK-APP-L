# notepad_controller.py - управление блокнотом
import pyautogui
import time
import random
import os
import config

def open_notepad(filepath):
    """Открывает блокнот с указанным файлом"""
    print(config.TEXT_OPENING)
    os.system(f'start notepad.exe "{filepath}"')
    time.sleep(config.NOTEPAD_OPEN_DELAY)

def maximize_notepad():
    """Разворачивает блокнот на весь экран"""
    pyautogui.hotkey('win', 'up')
    time.sleep(config.MAXIMIZE_DELAY)

def go_to_end_and_newline():
    """Переходит в конец файла и добавляет новую строку"""
    pyautogui.hotkey('ctrl', 'end')
    time.sleep(config.END_KEY_DELAY)
    pyautogui.press('enter')
    time.sleep(config.ENTER_DELAY)

def write_line(text):
    """Печатает строку в блокноте"""
    pyautogui.write(text)
    pyautogui.press('enter')

def save_file():
    """Сохраняет файл"""
    pyautogui.hotkey('ctrl', 's')
    time.sleep(config.SAVE_DELAY)

def micro_movement():
    """Маленькое движение мышкой в пределах блокнота"""
    x = config.MOUSE_BASE_X + random.randint(-config.MOUSE_MOVE_RANGE, config.MOUSE_MOVE_RANGE)
    y = config.MOUSE_BASE_Y + random.randint(-config.MOUSE_MOVE_RANGE, config.MOUSE_MOVE_RANGE)
    pyautogui.moveTo(x, y, duration=config.MOUSE_MOVE_DURATION)

def close_notepad():
    """Закрывает блокнот"""
    pyautogui.hotkey('alt', 'f4')