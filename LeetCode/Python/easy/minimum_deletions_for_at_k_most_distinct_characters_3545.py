"""
3545. Minimum Deletions for At Most K Distinct Characters
https://leetcode.com/problems/minimum-deletions-for-at-most-k-distinct-characters/
"""


class Solution:
    def minDeletion(self, s: str, k: int) -> int:
        count = 0
        freqs = Counter(s).most_common()
        while len(freqs) > k:
            count += freqs.pop()[1]
        return count
