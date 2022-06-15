"""
Sum of Parts
https://www.codewars.com/kata/5ce399e0047a45001c853c2b/train/python
"""


def parts_sums(ls):
    results = [sum(ls)]
    for i in range(len(ls)):
        results.append(results[i] - ls[i])
    return results
