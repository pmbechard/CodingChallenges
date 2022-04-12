"""
942. DI String Match
https://leetcode.com/problems/di-string-match/
"""

class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        result = [i for i in range(len(s) + 1)]
        while True:
            sorted = 0
            for i in range(len(s)):
                if s[i] == "I":
                    if result[i] > result[i+1]:
                        result[i], result[i+1] = result[i+1], result[i]
                    else:
                        sorted += 1
                else:
                    if result[i] < result[i+1]:
                        result[i], result[i+1] = result[i+1], result[i]
                    else:
                        sorted += 1
            if sorted == len(s):
                break
        return result

