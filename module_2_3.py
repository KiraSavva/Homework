my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
# for a in my_list:
    # if a >= 0:
    #     print(a)
    # else:
    #     break

a = 0
while a <= len(my_list) - 1:
    if my_list[a] > 0:
        print(my_list[a])
    elif my_list[a] < 0:
        break
    a += 1
