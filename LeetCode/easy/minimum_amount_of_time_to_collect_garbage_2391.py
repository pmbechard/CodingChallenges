"""
2391. Minimum Amount of Time to Collect Garbage
https://leetcode.com/problems/minimum-amount-of-time-to-collect-garbage/
"""


class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        g_index = -1
        p_index = -1
        m_index = -1
        for i in range(len(garbage)):
            if garbage[i].find("G") != -1:
                g_index = i
            if garbage[i].find("P") != -1:
                p_index = i
            if garbage[i].find("M") != -1:
                m_index = i

        g_string = "".join(garbage)
        g = g_string.count("G") + sum(travel[:g_index]) if g_index > -1 else 0
        p = g_string.count("P") + sum(travel[:p_index]) if p_index > -1 else 0
        m = g_string.count("M") + sum(travel[:m_index]) if m_index > -1 else 0

        return sum([g, p, m])
