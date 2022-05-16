"""
Integer depth
https://www.codewars.com/kata/59b401e24f98a813f9000026/train/python
"""

def compute_depth(n):
    depth = 1
    numbers = set([i for i in str(n)])
    while len(numbers) < 10:
        depth += 1
        factor = n * depth
        [numbers.add(i) for i in str(factor)]
    return depth
  
