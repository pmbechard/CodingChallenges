"""
1409. Queries on a Permutation With Key
https://leetcode.com/problems/queries-on-a-permutation-with-key/
"""


class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        perms = list(range(1, m+1))
        results = []
        for i in range(len(queries)):
            pos_in_perms = perms.index(queries[i])
            perms_val = perms[pos_in_perms]
            perms.remove(perms_val)
            perms.insert(0, perms_val)
            results.append(pos_in_perms)
        return results
