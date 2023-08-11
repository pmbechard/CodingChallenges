"""
2651. Calculate Delayed Arrival Time
https://leetcode.com/problems/calculate-delayed-arrival-time/
"""


class Solution:
    def findDelayedArrivalTime(self, arrivalTime: int, delayedTime: int) -> int:
        return (arrivalTime + delayedTime) % 24
