"""
3295. Report Spam Message
https://leetcode.com/problems/report-spam-message/
"""


class Solution:
    def reportSpam(self, message: List[str], bannedWords: List[str]) -> bool:
        freqs = Counter(message)
        total = 0
        for word in set(bannedWords):
            total += freqs[word]
        return total >= 2
