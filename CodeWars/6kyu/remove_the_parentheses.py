"""
Remove the parentheses
https://www.codewars.com/kata/5f7c38eb54307c002a2b8cc8/train/python
"""

def remove_parentheses(s):
    counter = 0
    result = ''
    for letter in s:
        if letter == '(':
            counter += 1
        elif letter == ')':
            counter -= 1
        else:
            result += letter
    return result
