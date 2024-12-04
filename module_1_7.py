
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
student = sorted(students) # сортировка списка
average_score = {}
# a = sum(grades[0]) /  len(grades[0]) # среднее арифметическое
# b = sum(grades[1]) /  len(grades[1])
# c = sum(grades[2]) /  len(grades[2])
# d = sum(grades[3]) /  len(grades[3])
# e = sum(grades[4]) /  len(grades[4])
# average_score = {student[0]: a, student[1]: b, student[2]: c, student[3]: d, student[4]: e}
# print(average_score)
for a in range(len(students)):
    b = sum(grades[a]) / len(grades[a])
    average_score[student[a]] = b
print(average_score)

