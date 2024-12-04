from math import trunc

my_dict = {"Kirill": 1996, "Vadim": 2002, "Anna": 2000}
print(my_dict)
print(my_dict["Kirill"])
print(my_dict.get("Lena"))
my_dict.update({"Dan": 1995, "Sasha": 2006})#Добавьте ещё две произвольные пары того же формата в словарь
print(my_dict)
a = my_dict.pop("Dan")   # Удалите одну из пар в словаре по существующему ключу из словаря my_dict
print(a)

my_set = {1,1,2,2, 'lol', 'lol', True, True}
print(my_set)
my_set.update({6,6,7,7,8,8})# Добавьте 2 произвольных элемента в множество my_set, которых ещё нет
print(my_set)
my_set.discard((2))             #Удалите один любой элемент из множества
print(my_set)