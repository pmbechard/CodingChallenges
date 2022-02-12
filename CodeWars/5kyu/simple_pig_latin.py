"""
Simple Pig Latin
https://www.codewars.com/kata/520b9d2ad5c005041100000f
"""


def pig_it(text):
    result = ''
    for word in text.split(' '):
        if word.isalpha():
            word = word[1:] + word[0] + 'ay'
        result += word + ' '
    return result.strip()
