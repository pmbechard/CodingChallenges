"""
1431. Kids With the Greatest Number of Candies
https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/
"""


class Solution:
    def kidsWithCandies(self, candies, extraCandies):
        results = []
        for i in candies:
            if i + extraCandies >= max(candies):
                results.append(True)
            else:
                results.append(False)
        return results
