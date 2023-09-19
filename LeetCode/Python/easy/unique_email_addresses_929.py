"""
929. Unique Email Addresses
https://leetcode.com/problems/unique-email-addresses/
"""


class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        uniq = set()
        for email in emails:
            split_email = email.split('@')
            local = split_email[0].replace('.', '')
            plus_index = local.find('+')
            if plus_index != -1:
                local = local[:plus_index]
            uniq.add(f'{local}@{split_email[1]}')
        return len(uniq)
