"""
2379. Minimum Recolors to Get K Consecutive Black Blocks
https://leetcode.com/problems/minimum-recolors-to-get-k-consecutive-black-blocks/
"""


class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        # min_recolors = k
        # for i in range(len(blocks) - k + 1):
        #     min_recolors = min(min_recolors, blocks[i:i + k].count('W'))
        # return min_recolors

        stack = list(blocks[:k])
        min_count = w_count = stack.count('W')
        for block in blocks[k:]:
            removed = stack.pop(0)
            if removed == 'W':
                w_count -= 1
            stack.append(block)
            if block == 'W':
                w_count += 1
            min_count = min(min_count, w_count)
        return min_count
