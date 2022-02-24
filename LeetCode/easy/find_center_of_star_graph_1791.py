"""
1791. Find Center of Star Graph
https://leetcode.com/problems/find-center-of-star-graph/
"""


class Solution:
    def findCenter(self, edges):
        return edges[0][0] if edges[0][0] in edges[1] else edges[0][1]
