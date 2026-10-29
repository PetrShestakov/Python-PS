# Задача-2:
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.
# Решение 1
one_list = [1, 2, 3, 4, 5]
other_list = [2, 3, 4, 5, 6, 7, 8]
for item in other_list:
     if item in one_list:
      one_list.remove(item)
print(one_list)
print(other_list)
# Решение 2
b = {'a', 'b', 'c', 'c', 'a', 'e'}
d = {'a', 'b', 'c', 'd'}
c = b - d
print(list(c))
