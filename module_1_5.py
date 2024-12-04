from math import trunc

immutable_var = 1, True, "Banana"
print(immutable_var)
#immutable_var[0] = 2 - кортеж не поддерживает обращение по элементам

mutable_list = ([1+2], 'Print', False)
print(mutable_list)
mutable_list[0][0] = 5
print(mutable_list)