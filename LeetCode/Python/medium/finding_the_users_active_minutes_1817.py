"""
1817. Finding the Users Active Minutes
https://leetcode.com/problems/finding-the-users-active-minutes/
"""


class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        uam_dict = dict()
        for i in logs:
            if i[0] in uam_dict.keys() and i[1] not in uam_dict[i[0]]:
                uam_dict[i[0]].append(i[1])
            elif i[0] not in uam_dict.keys():
                uam_dict[i[0]] = [i[1]]
        result = [0 for i in range(k)]
        for k, v in uam_dict.items():
            result[len(v) - 1] += 1
        return result
