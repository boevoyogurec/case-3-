# func.py - модуль для импорта функций для решения задачи
# TODO Добавить импорты внешних зависимостей
# import <название зависимости>
def input_excel_file(file_path): 
    # Загружаем исходный файл 
    input_file = file_path 
    # Читаем его из excrl 
    df = pd.read_excel(input_file) 
    return df