"""
Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону
(т.е. не меньше заданного минимума и не больше заданного максимума)
"""

lst = list(map(int, input("Введите элементы массива(через пробел): ").split(" ")))
min_el = int(input("Введите минимальное значение: "))
max_el = int(input("Введите максимальное значение: "))


"""
res_lst = []
for i in range(len(lst)):
    if min_el <= lst[i] <= max_el:
        res_lst.append(i)
print(res_lst)
"""

res_lst = [i for i in range(len(lst)) if min_el <= lst[i] <= max_el]
print(res_lst)
