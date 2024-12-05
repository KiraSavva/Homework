numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
prime = []
not_prime = []
is_prime = True
for i in numbers:
    for j in range(1, i - 1):
        if (i % j) == 0 and j != 1:
            is_prime = False
            not_prime.append(i)
            break
    else:
        prime.append(i)
print("Prime:", prime)
print("Not Prime:", not_prime)

