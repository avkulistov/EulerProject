
def mult_pif():
    for a in range(1, 500):
        for b in range(a + 1, 500):
            c = (1000 - a - b)
            if a * a + b * b == c ** 2:
                print(a, b, c, '--->', a * b * c)


mult_pif()
