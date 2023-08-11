"""
811. Subdomain Visit Count
https://leetcode.com/problems/subdomain-visit-count/
"""


class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        dic = dict()
        for domain in cpdomains:
            domain = domain.split(' ')
            while domain:
                dic[domain[1]] = dic.get(domain[1], 0) + int(domain[0])
                index = domain[1].find('.')
                if index == -1: break
                domain[1] = domain[1][index + 1:]
        return [f'{v} {k}' for k, v in dic.items()]
