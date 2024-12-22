
# func.py - модуль для импорта функций для решения задачи
# TODO Добавить импорты внешних зависимостей
import pandas as pd
from openpyxl import load_workbook

def input_excel_file(file_path): 
    # Загружаем исходный файл 
    input_file = file_path 
    # Читаем его из excrl 
    df = pd.read_excel(input_file) 
    return df

def clean_phone_number(phone):
    # Преобразуем значение в строку, если оно число
    if isinstance(phone, int) or isinstance(phone, float):
        phone = str(int(phone))
    # Убираем все символы кроме цифр
    return ''.join([char for char in phone if char.isdigit()])