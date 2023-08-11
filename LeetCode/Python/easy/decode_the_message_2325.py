"""
2325. Decode the Message
https://leetcode.com/problems/decode-the-message/
"""


class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        key_list = list(dict.fromkeys([i for i in key.replace(' ', '')]))
        output = ''
        for i in message:
            if i == ' ':
                output += ' '
            else:
                output += chr(key_list.index(i) + 97)
        return output
