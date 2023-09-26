"""
2865. Beautiful Towers I
https://leetcode.com/problems/beautiful-towers-i/
"""


class Solution:
    def maximumSumOfHeights(self, maxHeights: List[int]) -> int:
        max_sum = 0
        for i in range(len(maxHeights)):
            l, r = i - 1, i + 1
            current_sum = maxHeights[i]
            prev = maxHeights[i]
            while l >= 0:
                prev = min(maxHeights[l], prev)
                current_sum += prev
                l -= 1
            prev = maxHeights[i]
            while r < len(maxHeights):
                prev = min(maxHeights[r], prev)
                current_sum += prev
                r += 1
            if current_sum > max_sum:
                max_sum = current_sum
        return max_sum
