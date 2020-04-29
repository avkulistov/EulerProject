
def dev_sum_sqr(n):
    sum_sqr = 0
    sqr_sum = 0
    for i in range(n + 1):
        sum_sqr += i ** 2
        sqr_sum += i
    sqr_sum = sqr_sum ** 2

    print(sum_sqr)
    print(sqr_sum)
    return abs(sum_sqr - sqr_sum)


print(dev_sum_sqr(100))
