"""
2363. Merge Similar Items
https://leetcode.com/problems/merge-similar-items/
"""


class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        dic = dict()
        items = items1 + items2
        for i in range(len(items)):
            if dic.get(items[i][0]):
                dic[items[i][0]] += items[i][1]
            else:
                dic[items[i][0]] = items[i][1]
        return sorted(dic.items(), key=lambda x: x[0])