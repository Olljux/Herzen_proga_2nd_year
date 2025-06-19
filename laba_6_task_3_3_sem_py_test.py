
from configparser import ConfigParser, NoSectionError, NoOptionError
import csv

DEFAULT_PARAMS = {
    'precision': 0.00001,
    'dest': 'calc-history.csv'
}


def load_params_cp(file="params.ini"):

    params = DEFAULT_PARAMS.copy()

    parser = ConfigParser()

    read_files = parser.read(file)
    if not read_files:
        raise FileNotFoundError(f"Не удалось прочитать файл '{file}'")

    try:
        raw_prec = parser.get('DEFAULT', 'precision')
        raw_dest = parser.get('DEFAULT', 'dest')
    except (NoSectionError, NoOptionError) as e:
        raise KeyError(f"В файле '{file}' нет секции/ключа: {e}") from e

    try:
        precision = float(raw_prec)
    except ValueError as e:
        raise ValueError(f"Неверный формат числа precision='{raw_prec}'") from e

    params['precision'] = precision
    params['dest'] = raw_dest

    return params


def write_log_csv(*args, action=None, result=None, file='calc-history.csv'):

    row = [action] + list(args) + [result]

    try:
        with open(file, mode='a', newline='', errors='ignore') as f:
            writer = csv.writer(f)
            writer.writerow(row)
    except (PermissionError, FileNotFoundError) as e:
        backup = file.replace('.csv', '') + '.bak.csv'
        try:
            with open(backup, mode='a', newline='', errors='ignore') as f2:
                writer = csv.writer(f2)
                writer.writerow(row)
        except (PermissionError, FileNotFoundError) as e2:
            raise e2