"""
1710. Maximum Units on a Truck
https://leetcode.com/problems/maximum-units-on-a-truck/
"""


class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes = sorted(boxTypes, key=lambda x: -x[1])
        result = 0
        for boxType in boxTypes:
            num_boxes = min(truckSize, boxType[0])
            truckSize -= num_boxes
            result += num_boxes * boxType[1]
            if truckSize == 0:
                return result
        return result
