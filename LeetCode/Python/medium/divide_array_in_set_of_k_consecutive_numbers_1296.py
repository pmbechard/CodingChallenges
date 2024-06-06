"""
1296. Divide Array in Sets of K Consecutive Numbers
https://leetcode.com/problems/divide-array-in-sets-of-k-consecutive-numbers/
"""


class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        to_del = Counter()
        nums.sort()
        for num in nums:
            if num in to_del:
                to_del[num] -= 1
                if to_del[num] == 0:
                    del to_del[num]
            else:
                to_del.update({i: 1 for i in range(num + 1, num + k)})
        return False if to_del else True
