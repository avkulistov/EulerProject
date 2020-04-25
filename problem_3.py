from math import sqrt


def decor(func):
    def inner_dec(n):
        print('test decorator')
        print('sqrt n: ' + str(sqrt(n) + 1))
        return func(n)
    return inner_dec


@decor
def get_simple_dev_list(n):
    simple_dev_list = []
    dev_list = [dev_i for dev_i in range(1, int(sqrt(n) + 2), 2) if n % dev_i == 0]    # [dev_i for dev_i in range(1, n // 2 + 1, 2) if n % dev_i == 0]
    dev_list.insert(1, 2)
    dev_list.append(n)
    for i in dev_list:
        count = 0
        for j in range(1, i + 1):
            if i % j == 0:
                count += 1
            if i != j and count == 2:
                break
            elif i == j and count == 2:
                simple_dev_list.append(i)
    return simple_dev_list


n = int(input('Enter int number: '))
# simple_dev_list = get_simple_dev_list(13195)
# simple_dev_list = get_simple_dev_list(600851475143)
simple_dev_list = get_simple_dev_list(n)
print(simple_dev_list)
print(simple_dev_list[-1])
