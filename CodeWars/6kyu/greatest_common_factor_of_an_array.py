"""
Greatest Common Factor of an Array
https://www.codewars.com/kata/5849169a6512c5964000016e
"""


def greatest_common_factor(seq):
    result = 0
    for i in range(1, min(seq)+1):
        if not any([num % i for num in seq]):
            result = i
    return result
