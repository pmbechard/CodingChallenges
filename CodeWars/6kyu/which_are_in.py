"""
Which are in?
https://www.codewars.com/kata/550554fd08b86f84fe000a58
"""


def in_array(array1, array2):
    result = []
    for x in array1:
        for y in array2:
            if x in y and x not in result:
                result += [x]
    return sorted(result)
