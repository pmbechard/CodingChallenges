"""
661. Image Smoother
https://leetcode.com/problems/image-smoother/
"""


class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        new_img = []
        for row in range(len(img)):
            new_img.append([])
            for col in range(len(img[row])):
                surrounding = self.get_surrounding(img, row, col)
                new_img[-1].append(sum(surrounding) // len(surrounding))
        return new_img

    def get_surrounding(self, mat, row, col):
        output = [mat[row][col]]
        if row > 0 and col > 0:
            output.append(mat[row - 1][col - 1])
        if row > 0 and col < len(mat[0]) - 1:
            output.append(mat[row - 1][col + 1])
        if row < len(mat) - 1 and col > 0:
            output.append(mat[row + 1][col - 1])
        if row < len(mat) - 1 and col < len(mat[0]) - 1:
            output.append(mat[row + 1][col + 1])

        if row > 0:
            output.append(mat[row - 1][col])
        if row < len(mat) - 1:
            output.append(mat[row + 1][col])
        if col > 0:
            output.append(mat[row][col - 1])
        if col < len(mat[0]) - 1:
            output.append(mat[row][col + 1])

        return output
