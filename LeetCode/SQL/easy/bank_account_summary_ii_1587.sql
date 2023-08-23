# 1587. Bank Account Summary II
# https://leetcode.com/problems/bank-account-summary-ii/

# Write your MySQL query statement below
SELECT Users.name, SUM(Transactions.amount) as balance
FROM Users
LEFT JOIN Transactions
ON Users.account = Transactions.account
GROUP BY Transactions.account
HAVING SUM(Transactions.amount) > 10000;