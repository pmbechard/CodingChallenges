"""
8. String to Integer (atoi)
https://leetcode.com/problems/string-to-integer-atoi/
"""


class Solution:
    def myAtoi(self, s):
        s = s.strip()
        is_negative = False
        if not s:
            return 0
        if s[0] == '-':
            is_negative = True
            s = s[1:]
        elif s[0] == '+':
            s = s[1:]
        result = ""
        for i in s:
            if i.isnumeric():
                result += i
            else:
                break
        if not result:
            return 0
        result = int(result)
        result = result * - 1 if is_negative else result
        if result >= 2**31-1:
            result = 2**31-1
        elif result <= -2**31:
            result = -2 ** 31
        return result



solution = Solution()
print(solution.myAtoi("42"))                        # 42
print(solution.myAtoi("   -42"))                    # -42
print(solution.myAtoi("4193 with words"))           # 4193
