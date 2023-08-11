"""
2073. Time Needed to Buy Tickets
https://leetcode.com/problems/time-needed-to-buy-tickets/
"""


class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        front = 0
        counter = 0
        while tickets[k] > 0:
            counter += 1
            tickets[front] -= 1
            if tickets[front] == 0:
                if k == front: return counter
                tickets = tickets[:front] + tickets[front+1:]
                if k > front: k -= 1
            else:
                front += 1
            if front == len(tickets):
                front = 0
        return counter
