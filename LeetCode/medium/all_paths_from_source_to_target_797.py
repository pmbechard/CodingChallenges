"""
797. All Paths From Source to Target
https://leetcode.com/problems/all-paths-from-source-to-target/
"""


class Solution:
    def __init__(self):
        self.paths = []

    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        self.traversePaths(0, graph, [0])
        return self.paths

    def traversePaths(self, index, graph, path):
        if index == len(graph) - 1:
            self.paths.append(path)
        else:
            for i in graph[index]:
                self.traversePaths(i, graph, path + [i])
