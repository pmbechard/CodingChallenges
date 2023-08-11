"""
2739. Total Distance Traveled
https://leetcode.com/problems/total-distance-traveled/
"""


class Solution:
    def distanceTraveled(self, mainTank: int, additionalTank: int) -> int:
        distance = 0
        counter = 0
        while mainTank > 0:
            mainTank -= 1
            distance += 10
            counter += 1
            if counter == 5 and additionalTank > 0:
                mainTank += 1
                additionalTank -= 1
                counter = 0
        return distance
