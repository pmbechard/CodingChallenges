"""
Break camelCase
https://www.codewars.com/kata/5208f99aee097e6552000148
"""

def solution(s):
    s = list(s)
    for i in range(len(s)+1):
        if s[i].isupper() and s[i] is not s[0] and s[i-1] != ' ':
            s.insert(i, ' ')
    return ''.join(map(str, s))
