"""
165. Compare Version Numbers
https://leetcode.com/problems/compare-version-numbers
"""


class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        version1, version2 = version1.split('.'), version2.split('.')
        if len(version1) > len(version2):
            longer, shorter = version1, version2
        else:
            longer, shorter = version2, version1
        while len(longer) > len(shorter):
            shorter += [0]

        for i in range(len(version1)):
            int1, int2 = int(version1[i]), int(version2[i])
            if int1 > int2:
                return 1
            elif int1 < int2:
                return -1
        return 0
