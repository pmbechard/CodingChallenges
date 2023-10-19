"""
1629. Slowest Key
https://leetcode.com/problems/slowest-key/
"""


class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        max_key_time = (keysPressed[0], releaseTimes[0])
        for i in range(1, len(releaseTimes)):
            current = releaseTimes[i] - releaseTimes[i - 1]
            if current > max_key_time[1] or (current == max_key_time[1] and keysPressed[i] > max_key_time[0]):
                max_key_time = (keysPressed[i], current)
        return max_key_time[0]
