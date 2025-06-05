"""
3403. Find the Lexicographically Largest String From the Box I
https://leetcode.com/problems/find-the-lexicographically-largest-string-from-the-box-i/
"""


class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        if len(word) == numFriends:
            return max(list(word))
        elif numFriends == 1:
            return word
        max_len = len(word) - numFriends + 1
        target = max(set(word))
        output = ''
        for i in range(len(word)):
            if word[i] == target:
                output = self.maxStr(output, word[i : i + max_len])
        return output

    def maxStr(self, a, b):
        for i in range(min(len(a), len(b))):
            if a[i] > b[i]:
                return a
            elif b[i] > a[i]:
                return b
        return a if len(a) > len(b) else b
