"""
3000. Maximum Area of Longest Diagonal Rectangle
https://leetcode.com/problems/maximum-area-of-longest-diagonal-rectangle/
"""


class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        large = (self.diag(dimensions[0]), dimensions[0])
        for dim in dimensions[1:]:
            diag = self.diag(dim)
            if diag > large[0] or (diag == large[0] and self.area(dim) > self.area(large[1])):
                large = (diag, dim)
        return self.area(large[1])

    def diag(self, dim):
        return sqrt(dim[0]**2 + dim[1]**2)

    def area(self, dim):
        return dim[0] * dim[1]
