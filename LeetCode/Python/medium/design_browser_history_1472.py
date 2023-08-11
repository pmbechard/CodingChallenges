"""
1472. Design Browser History
https://leetcode.com/problems/design-browser-history/
"""


class BrowserHistory:

    def __init__(self, homepage: str):
        self.history = [homepage]
        self.pos = 0

    def visit(self, url: str) -> None:
        self.history = self.history[:self.pos + 1]
        self.history.append(url)
        self.pos += 1

    def back(self, steps: int) -> str:
        self.pos = max(0, self.pos - steps)
        return self.history[self.pos]

    def forward(self, steps: int) -> str:
        self.pos = min(len(self.history) - 1, self.pos + steps)
        return self.history[self.pos]

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
