"""
Corner Fill
https://www.codewars.com/kata/60b7d7c82358010006c0cda5
"""


def corner_fill(square):
    result = []
    while square:
        result += [i for i in square[0]]
        del square[0]

        if len(square) >= 1:
            for i in square:
                result.append(i[-1])
                del i[-1]
        if len(square) >= 1:
            for i in square[::-1]:
                result.append(i[-1])
                del i[-1]
        if len(square) >= 1:
            result += [i for i in reversed(square[0])]
            del square[0]

    return result
