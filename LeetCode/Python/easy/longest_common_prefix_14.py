"""
14. Longest Common Prefix
https://leetcode.com/problems/longest-common-prefix/
"""


class Solution:
    def longestCommonPrefix(self, strs):
        strs.sort(key=len)
        if len(strs) == 1 or not all(strs):
            return min(strs, key=len)
        end_index = 1
        prefix = ""
        while True:
            for i in strs:
                if end_index - 1 == len(i) or i[0:end_index] != strs[0][0:end_index]:
                    return prefix
            prefix += strs[0][end_index-1]
            end_index += 1

solution = Solution()
print(solution.longestCommonPrefix(["flower","flow","flight"]))       # "fl"
print(solution.longestCommonPrefix(["dog","racecar","car"]))          # ""
