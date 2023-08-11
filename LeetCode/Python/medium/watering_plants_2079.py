"""
2079. Watering Plants
https://leetcode.com/problems/watering-plants/
"""


class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        in_can = capacity
        steps = 0
        for i in range(len(plants)):
            if plants[i] > in_can:
                steps += i * 2 + 1
                in_can = capacity - plants[i]
            else:
                steps += 1
                in_can -= plants[i]
        return steps
