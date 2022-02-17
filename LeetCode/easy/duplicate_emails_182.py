"""
182. Duplicate Emails
https://leetcode.com/problems/duplicate-emails/
"""

# MySQL

SELECT email
FROM Person
GROUP BY email
HAVING COUNT(email) > 1;
