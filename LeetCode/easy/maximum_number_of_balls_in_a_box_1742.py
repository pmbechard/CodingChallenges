"""
1742. Maximum Number of Balls in a Box
https://leetcode.com/problems/maximum-number-of-balls-in-a-box/description/
"""


class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        balls = [str(x) for x in range(lowLimit, highLimit + 1)]
        result_dict = dict()
        for ball in balls:
            num = sum([int(x) for x in ball])
            if result_dict.get(num):
                result_dict[num] += 1
            else:
                result_dict[num] = 1
        return max(list(result_dict.values()))
