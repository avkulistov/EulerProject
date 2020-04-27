from datetime import datetime

def find_max_polindrom():
    max_num = 0
    for i in range(100, 1000):
        for j in range(100, 1000):
            num = i * j
            if str(num) == str(num)[::-1] and max_num < num:
                max_num = num

    return max_num


def find_max_polindrom_1():
    return max(i*j for i in range(100, 1000) for j in range(100, 1000) if str(i*j) == str(i*j)[::-1])

start_time = datetime.now()
print(find_max_polindrom())
print('time = ' + str(datetime.now() - start_time))

start_time = datetime.now()
print(find_max_polindrom_1())
print('time = ' + str(datetime.now() - start_time))