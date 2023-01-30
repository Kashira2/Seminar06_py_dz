# в файле находится N натуральных чисел, записанных через пробел.
# Средчисел не хватает одного, чтобы выполнялось услловие:
# A[i] - 1 = A[i-1]. Найдите это число.


# data = '1 2 3 4 5 6 8 9 10'.split()
# new_data = list(map(int, data))

# # for i in range(len(new_data) - 1):
# #     if not new_data[i] + 1 == new_data[i+1]:
# #         print(new_data[i] + 1)


# my_func = list(filter(lambda i: not new_data[i] + 1 == new_data[i+1], range(len(new_data) - 1)))

# for item in new_data:
#     print(new_data[item] + 1)

############################################################################################
# Дан список чисел. Создайте список, в который попадают числа, описываемые возрастающую последовательность. Порядок элементов менять нельзя.
# *Пример:*
# [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3] или [1, 7] или [1, 6, 7] и т.д.

data = [1, 5, 2, 3, 4, 6, 1, 7]

result = []
count = 0
num1 = 1
while count < len(data):
    for i in range(len(data) - 1):
        temp = []
        temp.append(data[i])
        cur_max = data[i]
        for j in range(num1, len(data)):
            if cur_max < data[j]:
                cur_max = data[j]
                temp.append(data[j])
        if len(temp) > 1 and temp not in result:
            result.append(temp)

    count += 1
    num1 += 1
print(result)







