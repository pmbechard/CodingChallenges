"""
3242. Design Neighbor Sum Service
https://leetcode.com/problems/design-neighbor-sum-service/
"""


class NeighborSum:

    def __init__(self, grid: List[List[int]]):
        self.grid = grid
        self.pos = dict()
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                self.pos[grid[row][col]] = [row, col]

    def adjacentSum(self, value: int) -> int:
        total = 0
        row, col = self.pos[value][0], self.pos[value][1]
        if row > 0:
            total += self.grid[row - 1][col]
        if row < len(self.grid) - 1:
            total += self.grid[row + 1][col]
        if col > 0:
            total += self.grid[row][col - 1]
        if col < len(self.grid) - 1:
            total += self.grid[row][col + 1]
        return total

    def diagonalSum(self, value: int) -> int:
        total = 0
        row, col = self.pos[value][0], self.pos[value][1]
        if row > 0 and col > 0:
            total += self.grid[row - 1][col - 1]
        if row > 0 and col < len(self.grid[row]) - 1:
            total += self.grid[row - 1][col + 1]
        if row < len(self.grid) - 1 and col < len(self.grid[row]) - 1:
            total += self.grid[row + 1][col + 1]
        if row < len(self.grid) - 1 and col > 0:
            total += self.grid[row + 1][col - 1]
        return total

# Your NeighborSum object will be instantiated and called as such:
# obj = NeighborSum(grid)
# param_1 = obj.adjacentSum(value)
# param_2 = obj.diagonalSum(value)
