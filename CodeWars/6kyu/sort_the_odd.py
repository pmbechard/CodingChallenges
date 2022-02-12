"""
Sort the odd
https://www.codewars.com/kata/578aa45ee9fd15ff4600090d
"""


def sort_array(source_array):
    array = source_array[:]
    array = sorted([x for x in array if x % 2 != 0])
    for n in range(len(source_array)):
        if source_array[n] % 2 != 0:
            source_array[n] = array[0]
            del array[0]
    return source_array
