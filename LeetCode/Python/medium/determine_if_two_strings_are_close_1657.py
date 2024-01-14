"""
1657. Determine if Two Strings Are Close
https://leetcode.com/problems/determine-if-two-strings-are-close
"""


class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        counter_1, counter_2 = Counter(word1), Counter(word2)
        for char in set(word1).union(word2):
            found_match = False
            a, b = (counter_1, counter_2) if char in counter_1 else (counter_2, counter_1)
            if char in counter_1:
                val = a[char]
                for k, v in b.items():
                    if v == val:
                        found_match = True
                        del a[char]
                        del b[k]
                        break
            if not found_match:
                return False
        return True
