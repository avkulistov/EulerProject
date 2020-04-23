
def fibonacci(n):
    list_fib = [1, 2]
    ind_1 = 0
    ind_2 = 1
    while True:
        new_num = list_fib[ind_1] + list_fib[ind_2]
        if new_num >= n:
            return list_fib
        ind_1 += 1
        ind_2 += 1
        list_fib.append(new_num)


def even_summ(list_num):
    even_list = [i for i in list_num if i % 2 == 0]
    return sum(even_list)


def sum_even_fib(n):
    f1, f2, s = 0, 1 , 0
    while f2 < n:
        s = s + f2 if f2 % 2 == 0 else s
        f1, f2 = f2, f1 + f2
    return s


print(even_summ(fibonacci(4000000)))
print(sum_even_fib(4000000))