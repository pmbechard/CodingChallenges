"""
1854. Maximum Population Year
https://leetcode.com/problems/maximum-population-year/
"""


class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        alive = dict()
        for years in logs:
            for year in range(years[0], years[1]):
                alive[year] = alive.get(year, 0) + 1
        min_year = None
        max_pop = None
        for year, pop in alive.items():
            if not max_pop or pop > max_pop:
                min_year = year
                max_pop = pop
            elif pop == max_pop and year < min_year:
                min_year = year
        return min_year
