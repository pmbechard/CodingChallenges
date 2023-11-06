"""
1103. Distribute Candies to People
https://leetcode.com/problems/distribute-candies-to-people/
"""


class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        output = [0] * num_people
        i = 0
        while candies:
            output[i % num_people] += min(candies, i + 1)
            candies -= min(candies, i + 1)
            i += 1
        return output
