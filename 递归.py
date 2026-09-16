def sum_number(num):
    if num == 1:
        return 1
    return num + sum_number(num - 1)
sum1 = sum_number(4)
print(sum1)