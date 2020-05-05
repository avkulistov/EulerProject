
def is_simple(n):
    r = int(n ** (1 / 2) // 1 + 1)
    for i in range(2, r):
        if n % i == 0:
            return False
    return True


def sum_of_simple(n):
    simple_sum = 2
    for i in range(3, n, 2):
        if is_simple(i):
            simple_sum += i
    return simple_sum


def eratosthen(n):
    sieve = list(range(n))
    sieve[1] = 0
    for i in sieve[2:]:
        for j in range(i + i, len(sieve), i):
            sieve[j] = 0
    return sieve


# print(sum_of_simple(2000000))
print(sum(eratosthen(2000000)))
