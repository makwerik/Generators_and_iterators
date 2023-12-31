"""
Учебный проект по генераторам-итераторам
"""

"""Генератор списка"""
nums = [i ** 2 for i in range(11)]

"""Выражения-генераторы(удобны для работы с большим кол-вом данных, т.к не занимают память)"""
second_nums = (i for i in range(777))


def get_num():
    """Функция-генератор"""
    for i in range(10):
        yield i


for f in get_num():
    print(f)
