class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        # if len(s) < 3:
        #     return []
        # elif len(s) == 3:
        #     if len(set(s)) == 1:
        #         return [[0, 2]]
        #     else:
        #         return []

        # current_stack = []
        # groups = []
        # for i in range(len(s)):
        #     if not current_stack or s[current_stack[-1]] == s[i]:
        #         current_stack.append(i)
        #     else:
        #         if len(current_stack) >= 3:
        #             groups.append([current_stack[0], current_stack[-1]])
        #         current_stack = [i]
        # if len(current_stack) >= 3:
        #     groups.append([current_stack[0], current_stack[-1]])
        # return groups

        len_s = len(s)
        groups = []
        i = 0
        while i < len_s - 2:
            j = i + 1
            while j < len_s and s[j] == s[i]:
                j += 1
            if j - i >= 3:
                groups.append([i, j - 1])
            i = j
        return groups
