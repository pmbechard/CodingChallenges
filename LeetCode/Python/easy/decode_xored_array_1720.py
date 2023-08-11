"""
1720. Decode XORed Array
https://leetcode.com/problems/decode-xored-array/
"""


class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        result = [first]
        for i in range(len(encoded)):
            result.append(encoded[i] ^ result[-1])
        return result
