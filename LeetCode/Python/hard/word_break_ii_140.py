"""
140. Word Break II
https://leetcode.com/problems/word-break-ii/
"""


class Solution:
    def __init__(self):
        self.solutions = []

    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        prefixes = self.get_prefixes([], s, wordDict)
        while prefixes:
            prefix = prefixes.pop()
            new_prefix = self.get_prefixes(prefix, s, wordDict)
            if new_prefix:
                prefixes += new_prefix
        return self.solutions

    def get_prefixes(self, current_prefixes, s, words):
        current_s = s.removeprefix(''.join(current_prefixes))
        if not current_s:
            self.solutions.append(' '.join(current_prefixes))
            return []
        return [current_prefixes + [word] for word in words if current_s.startswith(word)]
