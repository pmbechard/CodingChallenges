"""
1534. Count Good Triplets
https://leetcode.com/problems/count-good-triplets/
"""


class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        l = 0
        r = len(arr) - 1
        triplets_indices = []

        while l <= len(arr) - 3:
            if abs(arr[l] - arr[r]) <= c:
                for i in arr[ l +1:r]:
                    if abs(arr[r] - i) <= b and abs(arr[l] - i) <= a:
                        triplets_indices.append([l, '-', r])
            if len(arr[l: r +1]) == 3:
                l += 1
                r = len(arr) - 1
            else:
                r -= 1

        return len(triplets_indices)
