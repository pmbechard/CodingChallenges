"""
2409. Count Days Spent Together
https://leetcode.com/problems/count-days-spent-together/
"""


class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        days_per_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        arriveAlice = [int(i) for i in arriveAlice.split('-')]
        leaveAlice = [int(i) for i in leaveAlice.split('-')]
        arriveBob = [int(i) for i in arriveBob.split('-')]
        leaveBob = [int(i) for i in leaveBob.split('-')]

        later_arrival = None
        if arriveAlice[0] != arriveBob[0]:
            later_arrival = arriveAlice if arriveAlice[0] > arriveBob[0] else arriveBob
        else:
            later_arrival = arriveAlice if arriveAlice[1] > arriveBob[1] else arriveBob

        earlier_departure = None
        if leaveAlice[0] != leaveBob[0]:
            earlier_departure = leaveAlice if leaveAlice[0] < leaveBob[0] else leaveBob
        else:
            earlier_departure = leaveAlice if leaveAlice[1] < leaveBob[1] else leaveBob

        if later_arrival[0] == earlier_departure[0]:
            return max(0, earlier_departure[1] - later_arrival[1] + 1)
        elif later_arrival[0] > earlier_departure[0]:
            return 0
        else:
            return (days_per_month[later_arrival[0] - 1] - later_arrival[1]) + sum(
                days_per_month[later_arrival[0]:earlier_departure[0] - 1]) + earlier_departure[1] + 1
