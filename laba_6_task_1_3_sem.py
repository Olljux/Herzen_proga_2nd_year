PARAMS = {'precision': 0.00001, 'dest': 'output.txt'}


def load_params(file="params.ini"):

    try:
        f = open(file, mode='r', errors='ignore')
        lines = f.readlines()
        f.close()
    except FileNotFoundError:
        print(f"Файл '{file}' не найден")
        raise
    except PermissionError:
        print(f"Нет прав на чтение файла '{file}'")
        raise

    for line in lines:
        text = line.strip()
        if '=' not in text:
            raise ValueError(f"В строке нет символа '='")
        param = text.split('=')
        val = param[1].strip('\n')
        val = param[1].strip()
        key = param[0].strip()
        if not key:
            raise ValueError(f"В строка пустой ключ")
        if key != 'dest':
            try:
                val = eval(val)
            except Exception:
                print(f"Невозможно распарсить значение '{val}' в строке")
                raise

        PARAMS[key] = val

    return PARAMS


def write_log(*args, action=None, result=None, file='calc-history.log.txt.txt'):

    line = f"{action}: {args} = {result}\n"
    try:
        f = open(file, mode='a', errors='ignore')
        f.write(line)
        f.close()
    except (PermissionError, FileNotFoundError):
        print(f"Ошибка записи в файл '{file}'")
        backup = file + '.txt'
        print(f"Попытка записать лог в файл с новым именем: '{backup}'")
        try:
            b = open(backup, mode='a', errors='ignore')
            b.write(line)
            b.close()
        except (PermissionError, FileNotFoundError):
            print(f"Не удалось записать лог и в '{backup}'")
            raise


def calculate(*args, **kwargs):

    print("PARAMS до загрузки:", PARAMS)

    load_params('params.ini')
    print("PARAMS после загрузки:", PARAMS)

    res = sum(args)

    try:
        write_log(*args, action='sum', result=res, file=PARAMS['dest'])
    except Exception as e:
        print("Не удалось записать лог:", e)
        print(f"sum: {args} = {res}")

if __name__ == '__main__':
    load_params('params.ini')
    print(PARAMS)
    calculate(1,2,3)