"""
2515. Shortest Distance to Target String in a Circular Array
https://leetcode.com/problems/shortest-distance-to-target-string-in-a-circular-array/
"""


class Solution:
    def closetTarget(self, words: List[str], target: str, startIndex: int) -> int:
        if target not in words: return -1
        if words[startIndex] == target: return 0
        l_index = startIndex - 1
        r_index = startIndex + 1 if startIndex + 1 < len(words) else 0
        count = 1
        while r_index != l_index:
            if words[l_index] == target or words[r_index] == target:
                return count
            else:
                l_index -= 1
                r_index += 1
                if r_index == len(words):
                    r_index = 0
                count += 1
