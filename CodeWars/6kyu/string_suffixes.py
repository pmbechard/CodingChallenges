"""
String Suffixes
https://www.codewars.com/kata/559d34cb2e65e765b90000f0/train/python
"""


def string_suffix(str_):
    result = len(str_)
    for i in range(1, len(str_)):
        index = 0
        while index < len(str_[i:]) and str_[i:][index] == str_[index]:
            result += 1
            index += 1
    return result
i