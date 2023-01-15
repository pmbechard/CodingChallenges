"""
2299. Strong Password Checker II
https://leetcode.com/problems/strong-password-checker-ii/
"""


class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        hasLower = False
        hasUpper = False
        hasDigit = False
        hasSpecial = False
        prev = ''

        for i in password:
            if i == prev:
                return False
            prev = i

            if i.islower(): hasLower = True
            if i.isupper(): hasUpper = True
            if i.isdigit(): hasDigit = True
            if i in "!@#$%^&*()-+": hasSpecial = True

        return hasLower and hasUpper and hasDigit and hasSpecial and len(password) >= 8
