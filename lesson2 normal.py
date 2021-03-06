import random
import re
from math import sqrt


# Задача-1:
# Дан список, заполненный произвольными целыми числами, получите новый список,
# элементами которого будут квадратные корни элементов исходного списка,
# но только если результаты извлечения корня не имеют десятичной части и
# если такой корень вообще можно извлечь
# Пример: Дано: [2, -5, 8, 9, -25, 25, 4] Результат: [3, 5, 2]
# Решение №1
my_list = [4, 9, 81, 59, -225,121, 440]
new_list = []
for item in my_list:
    if item > 0 and sqrt(item) % 1 == 0:
     new_list.append(int(sqrt(item)))
print(new_list)


# Задача-2: Дана дата в формате dd.mm.yyyy, например: 02.11.2013.
# Ваша задача вывести дату в текстовом виде, например: второе ноября 2013 года.
# Склонением пренебречь (2000 года, 2010 года)


def verbalize_date_in_russian(some_date_in_russian_format):
    """
   :param: dd.mm.yyyy string
   Attn: limitedly accepts days from 01 to 20
   returns a date verbalized in Russian
   """

    def check_date_format(some_date):
        if re.fullmatch("[0-3]\d.[01]\d.\d{4}", some_date):
            return some_date
        else:
            raise ValueError("The date should be passed exactly as \"dd.mm.yyyy\"")

    day_dict = {"01": "первое",
                "02": "второе",
                "03": "третье",
                "04": "четвертое",
                "05": "пятое",
                "06": "шестое",
                "07": "седьмое",
                "08": "восьмое",
                "09": "девятое",
                "10": "десятое",
                "11": "одиннадцатое",
                "12": "двенадцатое",
                "13": "тринадцатое",
                "14": "четырнадцатое",
                "15": "пятнадцатое",
                "16": "шестнадцатое",
                "17": "семнадцатое",
                "18": "восемнадцатое",
                "19": "девятнадцатое",
                "20": "двадцатое",
                }

    month_dict = {"01": "января",
                  "02": "февраля",
                  "03": "марта",
                  "04": "апреля",
                  "05": "мая",
                  "06": "июня",
                  "07": "июля",
                  "08": "августа",
                  "09": "сентября",
                  "10": "октября",
                  "11": "ноября",
                  "12": "декабря"
                  }

    check_date_format(some_date_in_russian_format)

    verbal_day = day_dict[some_date_in_russian_format[:2]]
    verbal_month = month_dict[some_date_in_russian_format[3:5]]
    digital_year = some_date_in_russian_format[-4:]

    print("{} {} {} года".format(verbal_day, verbal_month, digital_year))


# Задача-3: Напишите алгоритм, заполняющий список произвольными целыми числами
# в диапазоне от -100 до 100. В списке должно быть n - элементов.
# Подсказка:
# для получения случайного числа используйте функцию randint() модуля random

def n_random_numbers_list(n):
    some_list = []
    for i in range(n):
        some_list.append(random.randint(-100, 100))
    print("The generated list with {} random values is:".format(n), some_list)


# Задача-4: Дан список, заполненный произвольными целыми числами.
# Получите новый список, элементами которого будут:
# а) неповторяющиеся элементы исходного списка:
# например, lst = [1, 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 2, 4, 5, 6]
# б) элементы исходного списка, которые не имеют повторений:
# например, lst = [1 , 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 4, 6]

def remove_doubles():
    initial_list = []
    for i in range(10):
        initial_list.append(random.randint(0, 10))
    print("Initial list is", initial_list)
    print("Unique values are:", set(initial_list))
    no_rep = [x for x in initial_list if initial_list.count(x) == 1]
    print("The elements of the list that were listed only once are:", no_rep)


if __name__ == "__main__":
    rooted_list()
    verbalize_date_in_russian("09.05.1945")
    n_random_numbers_list(5)
    remove_doubles()


