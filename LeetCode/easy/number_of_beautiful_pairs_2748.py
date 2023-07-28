"""
2748. Number of Beautiful Pairs
https://leetcode.com/problems/number-of-beautiful-pairs/
"""


class Solution:
    def countBeautifulPairs(self, nums: List[int]) -> int:
        beautiful_pairs = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                i_factors = self.get_factors(int(str(nums[i])[0]))
                j_factors = self.get_factors(int(str(nums[j])[-1]))
                intersection = i_factors.intersection(j_factors)
                if len(intersection) == 1:
                    beautiful_pairs += 1
        return beautiful_pairs

    def get_factors(self, num: int) -> Set[int]:
        output = set()
        for i in range(1, num + 1):
            if num % i == 0:
                output.add(i)
        return output
