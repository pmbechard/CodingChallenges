"""
2273. Find Resultant Array After Removing Anagrams
https://leetcode.com/problems/find-resultant-array-after-removing-anagrams/
"""


class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        skip = []
        result = []
        for i in range(len(words)):
            if i in skip:
                continue
            result.append(words[i])
            for j in range(i, len(words)):
                if sorted(list(words[i])) == sorted(list(words[j])):
                    skip.append(j)
                else:
                    break
        return result
