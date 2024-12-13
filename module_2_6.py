import random
def result(n):
    res = ""
    pas = []
    for i in range(1, 10):
        pas.append(i)
        for j in range(2,20):
            if n % (i + j) == 0 and j not in pas:
                res += f'{i}{j}'
    return res
random_num = random.randint(3,20)
print(f'{random_num}-{result(random_num)}')










