"""
Sort the number sequence
https://www.codewars.com/kata/5816b76988ca9613cc00024f
"""


def sort_sequence(sequence):
    mut_copy = sequence[:]
    sub_lists = []
    results = []
    zeroes = mut_copy.count(0)
    for i in range(zeroes):
        sub_lists += [mut_copy[:mut_copy.index(0)+1]]
        mut_copy = mut_copy[mut_copy.index(0)+1:]
    for list in sub_lists:
        list.remove(list[-1])
        list = sorted(list)
        list.append(0)
        results += [list]
    results = sum(sorted(results, key=lambda result: sum(result)), [])
    return results
