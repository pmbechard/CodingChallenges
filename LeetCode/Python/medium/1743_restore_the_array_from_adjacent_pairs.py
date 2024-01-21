"""
1743. Restore the Array From Adjacent Pairs
https://leetcode.com/problems/restore-the-array-from-adjacent-pairs
"""


class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        dic = {}
        start = None
        for pair in adjacentPairs:
            dic[pair[0]] = dic.get(pair[0], []) + [pair[1]]
            dic[pair[1]] = dic.get(pair[1], []) + [pair[0]]
        current = None
        for k, v in dic.items():
            if len(v) == 1:
                current = k
                break
        result = []
        used = set()
        while True:
            result.append(current)
            used.add(current)
            next = [i for i in dic[current] if i not in used]
            if not next:
                break
            current = next[0]
        return result
