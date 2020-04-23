def summ_3_5(n):
    list_num = [item for item in range(n) if (item % 3 == 0 or item % 5 == 0)]
    return sum(list_num)

print(summ_3_5(1000))