# Здесь необходимо реализовать декоратор, print_result который принимает на вход функцию,
# вызывает её, печатает в консоль имя функции, печатает результат и возвращает значение
# Если функция вернула список (list), то значения должны выводиться в столбик
# Если функция вернула словарь (dict), то ключи и значения должны выводить в столбик через знак равно
# Пример из ex_4.py:

def print_result(func):
    def wrapper():
        result = func()
        if type(result) == list:
            print(func.__name__)
            for x in result: print(x)
        elif type(result) == dict:
            print(func.__name__)
            for i in result:
                print('{} = {}'.format(i, result[i]))
        else:
            print(func.__name__)
            print(result)
    return wrapper
