"""
2937. Make Three Strings Equal
https://leetcode.com/problems/make-three-strings-equal/
"""


class Solution:
    def findMinimumOperations(self, s1: str, s2: str, s3: str) -> int:
        if s1 == s2 == s3:
            return 0

        if not (s1[0] == s2[0] == s3[0]):
            return -1

        shortest = min(len(s1), len(s2), len(s3))
        for i in range(shortest):
            if not (s1[i] == s2[i] == s3[i]):
                i -= 1
                break

        return (len(s1) + len(s2) + len(s3)) - 3 * (i + 1)
