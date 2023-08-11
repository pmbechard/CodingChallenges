"""
1603. Design Parking System
https://leetcode.com/problems/design-parking-system/
"""


class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.big = big
        self.num_big = 0
        self.medium = medium
        self.num_med = 0
        self.small = small
        self.num_small = 0

    def addCar(self, carType):
        if carType == 1:
            if self.num_big >= self.big:
                return False
            else:
                self.num_big += 1
                return True
        elif carType == 2:
            if self.num_med >= self.medium:
                return False
            else:
                self.num_med += 1
                return True
        elif carType == 3:
            if self.num_small >= self.small:
                return False
            else:
                self.num_small += 1
                return True
