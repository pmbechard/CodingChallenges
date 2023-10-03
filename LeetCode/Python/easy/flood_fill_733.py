"""
733. Flood Fill
https://leetcode.com/problems/flood-fill/
"""


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        to_visit = [[sr, sc]]
        visited = []
        init_color = image[sr][sc]

        while to_visit:
            current = to_visit.pop()
            visited.append(current)
            if image[current[0]][current[1]] != init_color:
                continue
            else:
                image[current[0]][current[1]] = color
            if current[0] > 0:
                up = [current[0] - 1, current[1]]
                if up not in visited:
                    to_visit.append(up)
            if current[0] < len(image) - 1:
                down = [current[0] + 1, current[1]]
                if down not in visited:
                    to_visit.append(down)
            if current[1] > 0:
                left = [current[0], current[1] - 1]
                if left not in visited:
                    to_visit.append(left)
            if current[1] < len(image[0]) - 1:
                right = [current[0], current[1] + 1]
                if right not in visited:
                    to_visit.append(right)
        return image
