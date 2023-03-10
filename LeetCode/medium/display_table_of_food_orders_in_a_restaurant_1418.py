"""
1418. Display Table of Food Orders in a Restaurant
https://leetcode.com/problems/display-table-of-food-orders-in-a-restaurant/
"""


class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        map = dict()
        foods = set()
        for order in orders:
            foods.add(order[2])
            if not map.get(order[1], False):
                map[order[1]] = {order[2]: 1}
            else:
                map[order[1]][order[2]] = map[order[1]].get(order[2], 0) + 1
        foods = sorted(list(foods))
        tables = sorted(list(map.keys()), key=lambda x: int(x))
        print(tables)
        output = [["Table"]]
        for food in foods:
            output[0].append(food)
        for table in tables:
            output.append([table])
            for food in foods:
                output[-1].append(str(map[table].get(food, 0)))
        return output
