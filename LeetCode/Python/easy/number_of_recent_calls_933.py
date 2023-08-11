"""
933. Number of Recent Calls
https://leetcode.com/problems/number-of-recent-calls/
"""


class RecentCounter:

    def __init__(self):
        self.requests = []

    def ping(self, t: int) -> int:
        self.requests.append(t)
        counter = 0
        while t - self.requests[counter] > 3000:
            counter += 1
        self.requests = self.requests[counter:]
        return len(self.requests)

# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
