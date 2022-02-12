"""
Vowels Back
https://www.codewars.com/kata/57cfd92c05c1864df2001563
"""


def vowel_back(st):
    result = ''
    vowels = ['a', 'i', 'u']
    for letter in st:
        original = letter
        if letter == 'c' or letter =='o':
            letter = chr(ord(letter) - 1)
        elif letter  == 'd' or letter == 'e':
            letter = 'a'
        elif letter in vowels:
            letter = chr(ord(letter) - 5)
        else:
            letter = chr(ord(letter) + 9)
        if ord(letter) < 97:
            letter = chr(ord(letter) + 26)
        elif ord(letter) > 122:
            letter = chr(ord(letter) - 26)
        if letter in 'code':
            letter = original
        result += letter
    return result
