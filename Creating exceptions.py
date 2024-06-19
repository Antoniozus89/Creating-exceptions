class InvalidDataException(Exception):
    def __init__(self, message):
        self.message = message


def get_int(a):
    raise InvalidDataException('Аргумент должен быть в числовом формате')


try:
    get_int('привет')
except InvalidDataException as e:
    print(f"Сообщение об ошибке: {e.message}")


class ProcessingException(Exception):
    def __init__(self, message):
        self.message = message


def open_file():

    raise ProcessingException('Такого файла в данной системе нет')
try:
    open_file()
    file_name = 'Pyshkin.txt'
except ProcessingException as e:
    print(f"Собщение об ошибке: {e.message}")
    
