"""
Last Survivors Ep.2
https://www.codewars.com/kata/60a1aac7d5a5fc0046c89651
"""


def last_survivors(string):
    doubles = True
    while doubles:
        for l in string:
            print(l, string.count(l))
            if string.count(l) > 1:
                if l == 'z':
                    string = string.replace(l, 'a', 1)
                    string = string.replace(l, '', 1)
                else:
                    string = string.replace(l, chr(ord(l)+1), 1)
                    string = string.replace(l, '', 1)
        if len(list(string)) == len(set(string)):
            return string
