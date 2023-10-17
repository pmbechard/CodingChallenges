"""
2899. Last Visited Integers
https://leetcode.com/problems/last-visited-integers/
"""


class Solution:
    def lastVisitedIntegers(self, words: List[str]) -> List[int]:
        ints, result = [], []
        prev_count = 0
        for i in words:
            if i == 'prev':
                prev_count += 1
                if len(ints) >= prev_count:
                    result.append(ints[-1 * prev_count])
                else:
                    result.append(-1)
            else:
                prev_count = 0
                ints.append(int(i))
        return result
