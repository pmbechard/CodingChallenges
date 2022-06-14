"""
832. Flipping and Image
https://leetcode.com/problems/flipping-an-image/
"""

class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        result = []
        for i in range(len(image)):
            result.append([])
            for j in image[i][::-1]:
                if j == 1:
                    result[i].append(0)
                else:
                    result[i].append(1)
        return result
