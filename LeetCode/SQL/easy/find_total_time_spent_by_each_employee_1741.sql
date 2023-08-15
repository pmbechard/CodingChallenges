# 1741. Find Total Time Spent by Each Employee
# https://leetcode.com/problems/find-total-time-spent-by-each-employee/


# Write your MySQL query statement below
SELECT event_day as day, emp_id, SUM(out_time - in_time) as total_time
FROM Employees
GROUP BY emp_id, event_day;
