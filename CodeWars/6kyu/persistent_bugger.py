"""
Persistent Bugger.
https://www.codewars.com/kata/55bf01e5a717a0d57e0000ec
"""


def persistence(n):
    product = 1
    counter = 1
    n = str(n)
    if len(n) == 1:
        return 0
    while True:
        for i in n:
            product *= int(i)
        if product < 10:
            return counter
        counter += 1
        n = str(product)
        product = 1
