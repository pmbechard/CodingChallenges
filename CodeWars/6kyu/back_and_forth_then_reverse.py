"""
Back and forth then Reverse!
https://www.codewars.com/kata/60cc93db4ab0ae0026761232
"""


def arrange(s):
    t = []
    for i in range((len(s)) // 2):
        if i % 2 == 0:
            t += [s[i], s[i*-1-1]]
        else:
            t += [s[i * -1 - 1], s[i]]
    return t if len(s) % 2 == 0 else t + [s[len(s)//2]]
