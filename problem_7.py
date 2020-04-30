
def is_simple(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


def simple_num(n):
    count = 1
    i = 3
    while True:
        if n == 1:
            return 2
        elif is_simple(i):
            count += 1
        if count == n:
            return i
        i += 2


print(simple_num(10001))
