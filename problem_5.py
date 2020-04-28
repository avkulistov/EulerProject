from datetime import datetime
from math import gcd
from functools import reduce


def work_time(func):
    def inner_dec(a, b):
        start_time = datetime.now()
        print(func(a, b))
        print(datetime.now() - start_time)
    return inner_dec


#@work_time
def find_min_dev(a, b):
    min_num = b
    while True:
        count = 0
        
        for i in range(a, b + 1):
            if min_num % i != 0:
                break
            else:
                count += 1
        
        if count == b - a + 1:
            return min_num

        min_num += 1


#@work_time
def find_min_dev_1(a, b):
    min_num = 1
    
    for i in range(a, b + 1):
        min_num = min_num * i // gcd(i, min_num)
 
    return min_num



print(find_min_dev(1, 10))
print(find_min_dev_1(1, 10))
