"""
2405. Optimal Partition of String
https://leetcode.com/problems/optimal-partition-of-string/
"""


class Solution:
    def partitionString(self, s: str) -> int:
        partitions = ['']
        currentIndex = 0
        for i in range(len(s)):
            if not s[i] in partitions[currentIndex]:
                partitions[currentIndex] += s[i]
            else:
                partitions.append(s[i])
                currentIndex += 1
        return len(partitions)
