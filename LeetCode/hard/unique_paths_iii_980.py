"""
980. Unique Paths III
https://leetcode.com/problems/unique-paths-iii/
"""


class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        start, end, obstacles_count = self.get_start_and_end(grid)
        return self.traverse(grid, start, end, [], obstacles_count, 0)

    def traverse(self, grid, current, end, visited, obstacles_count, output):
        if current == end and len(visited) == len(grid) * len(grid[0]) - obstacles_count - 1:
            output += 1
        else:
            for move in self.get_available_moves(grid, current, visited):
                output = self.traverse(grid, move, end, visited + [current], obstacles_count, output)
        return output

    def get_start_and_end(self, grid):
        start = end = None
        obstacles_count = 0
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] == 1:
                    start = [row, col]
                elif grid[row][col] == 2:
                    end = [row, col]
                elif grid[row][col] == -1:
                    obstacles_count += 1
        return [start, end, obstacles_count]

    def get_available_moves(self, grid, current, visited):
        moves = []
        # right move availability
        if current[1] < len(grid[0]) - 1 and [current[0], current[1] + 1] not in visited and grid[current[0]][
            current[1] + 1] != -1:
            moves.append([current[0], current[1] + 1])
        # left move availability
        if current[1] > 0 and [current[0], current[1] - 1] not in visited and grid[current[0]][current[1] - 1] != -1:
            moves.append([current[0], current[1] - 1])
        # down move availability
        if current[0] < len(grid) - 1 and [current[0] + 1, current[1]] not in visited and grid[current[0] + 1][
            current[1]] != -1:
            moves.append([current[0] + 1, current[1]])
        # up move availability
        if current[0] > 0 and [current[0] - 1, current[1]] not in visited and grid[current[0] - 1][current[1]] != -1:
            moves.append([current[0] - 1, current[1]])
        return moves
