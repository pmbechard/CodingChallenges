"""
2614. Prime In Diagonal
https://leetcode.com/problems/prime-in-diagonal/
"""


class Solution:
    def diagonalPrime(self, nums: List[List[int]]) -> int:
        largest_prime = 0
        for i in range(len(nums)):
            num = nums[i][i]
            if num > largest_prime and self.is_prime(num):
                largest_prime = num
            num = nums[i][len(nums) - 1 - i]
            if num > largest_prime and self.is_prime(num):
                largest_prime = num
        return largest_prime

    def is_prime(self, num):
        if num <= 1: return False
        for i in range(2, num // 2):
            if num % i == 0: return False
        return True
