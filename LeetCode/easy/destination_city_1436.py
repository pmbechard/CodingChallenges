"""
1436. Destination City
https://leetcode.com/problems/destination-city/
"""


class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        from_to = [[], []]
        for i in paths:
            from_to[0].append(i[0])
            from_to[1].append(i[1])
        print(from_to)

        for i in from_to[1]:
            if i not in from_to[0]:
                return i