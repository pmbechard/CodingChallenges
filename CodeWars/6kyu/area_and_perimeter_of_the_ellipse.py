"""
Area and perimeter of the ellipse
https://www.codewars.com/kata/5830e7feff1a3ce8d4000062
"""


def ellipse(a, b):
    return f"Area: {round((3.14159265359*a*b), 1)}, perimeter: {round(3.14159265359*(3/2*(a+b)-(a*b)**0.5), 1)}"
