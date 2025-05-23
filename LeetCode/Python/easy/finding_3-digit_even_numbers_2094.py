"""
2094. Finding 3-Digit Even Numbers
https://leetcode.com/problems/finding-3-digit-even-numbers/
"""


class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        output = []
        ctr = Counter(digits)
        for num in range(100, 999, 2):
            snum = str(num)
            if snum.count(snum[0]) <= ctr[int(snum[0])] and snum.count(snum[1]) <= ctr[int(snum[1])] and snum.count(
                    snum[2]) <= ctr[int(snum[2])]:
                output.append(num)
        return output
