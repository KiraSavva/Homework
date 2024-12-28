def print_params(a = 1, b = "строка", c = True):
    print(a,b,c)
    print([],"list", False)
    print()

values_list = [2, True, "Hi"]
values_dict = {'a': 2, 'b': 'Hello', 'c': False}
print(*values_list)
print(*values_dict)

values_list_2 = [54.32, 'Строка']
print_params(*values_list_2, 42)




