"""
Pete, the baker
https://www.codewars.com/kata/525c65e51bf619685c000059
"""


def cakes(recipe, available):
    counter = sum([1 for i in available if i in recipe])
    if counter != len(recipe):
        return 0
    else:
        quantity = []
        for k, v in recipe.items():
            if available[k] - recipe[k] < 0:
                return 0
            else:
                quantity.append(available[k] // recipe[k])
    return min(quantity)
