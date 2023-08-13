# 181. Employees Earning More Than Their Managers
# https://leetcode.com/problems/employees-earning-more-than-their-managers/


# Write your MySQL query statement below
SELECT a.name as "Employee"
FROM Employee a
INNER JOIN Employee b ON a.managerId = b.id
WHERE a.salary > b.salary;