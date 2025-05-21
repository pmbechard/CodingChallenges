"""
93. Restore IP Addresses
https://leetcode.com/problems/restore-ip-addresses/
"""


class Solution:
    def __init__(self):
        self.combs = []

    def restoreIpAddresses(self, s: str) -> List[str]:
        self.traverse([], s)
        return self.combs

    def traverse(self, curr, s):
        if len(curr) > 4:
            return None
        if len(curr) == 4 and not s:
            self.combs.append('.'.join(curr))
            return
        for i in range(len(s)):
            val = s[:i + 1]
            if len(val) > 1 and val[0] == '0':
                continue
            if int(val) <= 255:
                self.traverse(curr + [val], s.removeprefix(val))
