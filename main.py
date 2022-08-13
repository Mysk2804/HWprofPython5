import datetime
import os


# def log_zodiac(old_function):
#     def new_function(*args, **kwargs):
#         date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#         zodiac = old_function(*args, **kwargs)
#         log = f'Дата: {date} Имя функции: {old_function.__name__} Аргументы: {args},{kwargs} Результат: {zodiac}\n'
#         with open('log_file.txt', 'a') as f:
#             f.write(log)
#         return old_function(*args, **kwargs)
#     return new_function
#

def log(file_path):
    def log_zodiac(old_function):
        def new_function(*args, **kwargs):
            date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            zodiac = old_function(*args, **kwargs)
            log = f'Дата: {date} Имя функции: {old_function.__name__} Аргументы: {args},{kwargs} Результат: {zodiac}\n'
            with open(file_path, 'a') as f:
                f.write(log)
            return old_function(*args, **kwargs)
        return new_function
    return log_zodiac


@log(os.path.join(os.getcwd(), 'log_file2.txt'))
def zodiac_fun(month, number):
    if month == 'Январь':
        if number >=20:
            zodiac = 'Козерог'
        else:
            zodiac = 'Водолей'
    elif month == 'Февраль':
        if number >= 19:
            zodiac = 'Рыбы'
        else:
            zodiac = 'Водолей'
    elif month == 'Март':
        if number >= 21:
            zodiac = 'Овен'
        else:
            zodiac = 'Рыбы'
    elif month == 'Апрель':
        if number >= 21:
            zodiac = 'Телец'
        else:
            zodiac = 'Овен'
    elif month == 'Май':
        if number >= 21:
            zodiac = 'Близнецы'
        else:
            zodiac = 'Телец'
    elif month == 'Июнь':
        if number >= 21:
            zodiac = 'Рак'
        else:
            zodiac = 'Близнецы'
    elif month == 'Июль':
        if number >= 23:
            zodiac = 'Лев'
        else:
            zodiac = 'Рак'
    elif month == 'Август':
        if number >= 23:
            zodiac = 'Дева'
        else:
            zodiac = 'Лев'
    elif month == 'Сентябрь':
        if number >= 23:
            zodiac = 'Весы'
        else:
            zodiac = 'Дева'
    elif month == 'Октябрь':
        if number >= 23:
            zodiac = 'Скорпион'
        else:
            zodiac = 'Весы'
    elif month == 'Ноябрь':
        if number >= 22:
            zodiac = 'Стрелец'
        else:
            zodiac = 'Скорпион'
    elif month == 'Декабрь':
        if number >= 22:
            zodiac = 'Козерог'
        else:
            zodiac = 'Стрелец'
    return zodiac


if __name__ == '__main__':
    zodiac_fun('Апрель', 28)
