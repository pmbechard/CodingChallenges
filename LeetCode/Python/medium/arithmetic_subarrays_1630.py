"""
1630. Arithmetic Subarrays
https://leetcode.com/problems/arithmetic-subarrays/
"""


class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        output = []
        for i in range(len(l)):
            seq = nums[l[i]:r[i]+1]
            seq.sort()
            diff = seq[0] - seq[1]
            for j in range(1, len(seq)-1):
                if seq[j] - seq[j+1] != diff:
                    output.append(False)
                    break
            if len(output) < i+1:
                output.append(True)
        return output
