"""
1282. Group the People Given the Group Size They Belong To
https://leetcode.com/problems/group-the-people-given-the-group-size-they-belong-to/
"""


class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        groups_dict = dict()
        for i in range(len(groupSizes)):
            if groups_dict.get(groupSizes[i]):
                groups_dict[groupSizes[i]].append(i)
            else:
                groups_dict[groupSizes[i]] = [i]

        results = []
        for key, value in groups_dict.items():
            current_values = value
            while len(current_values) != 0:
                results.append(current_values[:key])
                current_values = current_values[key:]

        return results
