"""
278. First Bad Version
https://leetcode.com/problems/first-bad-version/
"""


# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        low, high = 0, n - 1
        mid = (low + high) // 2
        while low <= high:
            if not isBadVersion(mid):
                if isBadVersion(mid + 1):
                    return mid + 1
                low = mid + 1
            else:
                high = mid - 1
            mid = low + (high - low) // 2
