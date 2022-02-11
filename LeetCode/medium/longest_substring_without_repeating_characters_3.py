"""
3. Longest Substring Without Repeating Characters
https://leetcode.com/problems/longest-substring-without-repeating-characters/
"""


class Solution:
    def lengthOfLongestSubstring(self, s):
        substring = ""
        largest_substring = 0

        for letter in s:
            if letter in substring:
                substring = substring[substring.index(letter) + 1:] + letter
            else:
                substring += letter
                if len(substring) > largest_substring:
                    largest_substring = len(substring)
        return largest_substring


solution = Solution()
print(solution.lengthOfLongestSubstring("abcabcbb"))        # 3 (abc)
print(solution.lengthOfLongestSubstring("bbbbb"))           # 1 (b)
print(solution.lengthOfLongestSubstring("pwwkew"))          # 3 (kew)
print(solution.lengthOfLongestSubstring("dvdf"))            # 3 (vdf)
