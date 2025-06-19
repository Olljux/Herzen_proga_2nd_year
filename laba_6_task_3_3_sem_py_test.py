import os
from configparser import ConfigParser, NoSectionError, NoOptionError
import csv

# По умолчанию эти параметры, если INI не будет найден или неполон
DEFAULT_PARAMS = {
    'precision': 0.00001,
    'dest': 'calc-history.csv'
}


def load_params_cp(file="params.ini"):
    """
    Читает параметры из INI‑файла через configparser.
    Ожидается файл с секцией [DEFAULT] и ключами:
      precision (float) и dest (str).
    Если файл не найден или не читается → FileNotFoundError, PermissionError.
    Если секции/ключа нет → KeyError.
    Если значение не конвертируется в float (для precision) → ValueError.
    Возвращает словарь params.
    """
    # Настройки по‑умолчанию
    params = DEFAULT_PARAMS.copy()

    parser = ConfigParser()

    # Попытка прочитать файл: возвращает список реально прочитанных имён
    read_files = parser.read(file)
    if not read_files:
        # Не нашли файл или нет прав на чтение
        raise FileNotFoundError(f"Не удалось прочитать файл '{file}'")

    try:
        # Читаем из секции DEFAULT
        raw_prec = parser.get('DEFAULT', 'precision')
        raw_dest = parser.get('DEFAULT', 'dest')
    except (NoSectionError, NoOptionError) as e:
        # Секция или ключ отсутствует
        raise KeyError(f"В файле '{file}' нет секции/ключа: {e}") from e

    # Конвертация precision в float
    try:
        precision = float(raw_prec)
    except ValueError as e:
        raise ValueError(f"Неверный формат числа precision='{raw_prec}'") from e

    # Собираем итоговый словарь
    params['precision'] = precision
    params['dest'] = raw_dest

    return params


def write_log_csv(*args, action=None, result=None, file='calc-history.csv'):
    """
    Записывает строчку лога в CSV‑файл.
    Формирует запись [action, *args, result].
    1) Открывает файл file на дозапись.
    2) При PermissionError/FileNotFoundError пробует file + '.bak.csv'.
    3) Если и там не удалось — пробрасывает исключение.
    """
    # Строка для записи: action, тотпы positional args, потом result
    row = [action] + list(args) + [result]

    try:
        # Открытие основного CSV‑файла
        with open(file, mode='a', newline='', errors='ignore') as f:
            writer = csv.writer(f)
            writer.writerow(row)
    except (PermissionError, FileNotFoundError) as e:
        # При проблемах записи в основной файл — резервный
        backup = file.replace('.csv', '') + '.bak.csv'
        try:
            with open(backup, mode='a', newline='', errors='ignore') as f2:
                writer = csv.writer(f2)
                writer.writerow(row)
        except (PermissionError, FileNotFoundError) as e2:
            # Ни в основных, ни в резервных файлах писать нельзя
            raise e2