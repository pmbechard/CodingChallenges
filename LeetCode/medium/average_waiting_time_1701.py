"""
1701. Average Waiting Time
https://leetcode.com/problems/average-waiting-time/
"""


class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        wait_total = 0
        end = customers[0][0]
        for customer in customers:
            overlap = end - customer[0] if end > customer[0] else 0
            end = (customer[0] + customer[1] + overlap)
            wait = end - customer[0]
            wait_total += wait
        return wait_total / len(customers)
