"""
728. Self Dividing Numbers
https://leetcode.com/problems/self-dividing-numbers/
"""

class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        results = []
        for i in range(left, right+1):
            if '0' in str(i):
                continue
            if all([i % int(l) == 0 for l in str(i)]):
                results.append(i)
        return results
