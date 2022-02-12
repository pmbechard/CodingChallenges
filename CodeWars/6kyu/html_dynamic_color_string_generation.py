"""
HTML dynamic color string generation
https://www.codewars.com/kata/56f1c6034d0c330e4a001059
"""


import random
def generate_color_rgb():
    result = ''
    options = [str(i) for i in range(0, 10)] + ['a','b','c','d','e','f']
    for i in range(6):
        result += random.choice(options)
    return f'#{result}'
