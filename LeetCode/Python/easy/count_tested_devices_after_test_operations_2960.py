"""
2960. Count Tested Devices After Test Operations
https://leetcode.com/problems/count-tested-devices-after-test-operations/
"""


class Solution:
    def countTestedDevices(self, batteryPercentages: List[int]) -> int:
        output = 0
        for i in batteryPercentages:
            if i - output > 0:
                output += 1
        return output
