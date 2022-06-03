"""
2120. Execution of All Suffix Instructions Staying in a Grid
https://leetcode.com/problems/execution-of-all-suffix-instructions-staying-in-a-grid/
"""


class Solution:
    def executeInstructions(self, n: int, startPos: List[int], s: str) -> List[int]:
        output = [0] * len(s)

        for i in range(len(s)):
            pos = startPos[:]
            current_index = i

            while current_index < len(s):
                if s[current_index] == 'R':
                    pos[1] += 1
                elif s[current_index] == 'L':
                    pos[1] -= 1
                elif s[current_index] == 'D':
                    pos[0] += 1
                elif s[current_index] == 'U':
                    pos[0] -= 1
                current_index += 1

                if 0 <= pos[0] < n and 0 <= pos[1] < n:
                    output[i] += 1
                else:
                    break
        return output
