# Задание-1:
# Дан список, заполненный произвольными целыми числами.
# Получить новый список, элементы которого будут
# квадратами элементов исходного списка
# [1, 2, 4, 0] --> [1, 4, 16, 0]

list_1 = [4, 22, 6, 7, 11, 0, 3, 5]
print('list_1:', list_1)
list_2 = list(map(lambda x: x ** 2, list_1))
print('list_2:', list_2)

# Задание-2:
# Даны два списка фруктов.
# Получить список фруктов, присутствующих в обоих исходных списках.

print('________________________________________')

fruit_list_1 = ['Апельсин', 'Мандарин', 'Яблоко', 'Киви', 'Лимон']
fruit_list_2 = ['Манго', 'Грейпфрут', 'Апельсин', 'Банан', 'Лимон', 'Киви']
result_list = [i for i in fruit_list_1 if i in fruit_list_2]
print(result_list)




#NORMAL
# Напишите скрипт, заполняющий указанный файл (самостоятельно задайте имя файла)
# произвольными целыми цифрами, в результате в файле должно быть
# 2500-значное произвольное число.
# Найдите и выведите самую длинную последовательность одинаковых цифр
# в вышезаполненном файле.
# import random


random_list = [random.randint(1, 5) for i in range(2500)]

# print(random_list)
str_random_list = ''.join([str(x) for x in random_list])
print(str_random_list)
print(len(str_random_list))
#making txt file with string of numbers
with open('random_string.txt', 'w') as r:
    r.write(str_random_list)
counter = ''
sorted_and_grouped = []
for i in range(len(str_random_list)-1):
    # if items repeat, append them to a string
    if str_random_list[i] == str_random_list[i+1]:
        counter += str(str_random_list[i])
    else:
        #if not repeats append lonely (we always append here/ because [5556] --> 5!= 6, but we have to append it
        counter += str(str_random_list[i])
        sorted_and_grouped.append(counter)
        counter = ''
# print(sorted_and_grouped)
# We are counting length of every item in the list
# list_lengthes == sorted_and_groepd by indexes, nubbers are different, but indexes THE SAME
list_lengthes = (list(map(len, sorted_and_grouped)))
# print(list_lengthes)
print(f'len of list_lenthes= {len(list_lengthes)} == len of sorted_and_grouped= {len(sorted_and_grouped)}')
#find the biggest length
max_number_of_repeats = max(list_lengthes)
print(f'max number repeats= {max_number_of_repeats}')
#find out index of the biggest repeat
index_of_max_repeats = list_lengthes.index(max_number_of_repeats)
#ask for a final longest string by its index
biggest_number = sorted_and_grouped[index_of_max_repeats]
print(f'The biggest number= {biggest_number}')
# new_list = [str(x) for x in list_lengthes]
# print(list(map(max, new_list)))