"""
2. Add Two Numbers
https://leetcode.com/problems/add-two-numbers/submissions/
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1, l2):
        l1_str = self.toString(l1)
        l2_str = self.toString(l2)
        ll_sum = int(l1_str) + int(l2_str)
        ll_sum = str(ll_sum)
        result = ListNode(val=int(ll_sum[-1]))
        current_node = result
        for i in reversed(ll_sum[:-1]):
            current_node.next = ListNode(val=i)
            current_node = current_node.next
        return result

    def toString(self, ll):
        result = ""
        while ll.next:
            result = str(ll.val) + result
            ll = ll.next
        result = str(ll.val) + result
        return result


l13 = ListNode(val=3, next=None)
l12 = ListNode(val=4, next=l13)
l11 = ListNode(val=2, next=l12)

l23 = ListNode(val=4, next=None)
l22 = ListNode(val=6, next=l23)
l21 = ListNode(val=5, next=l22)

solution = Solution()
example = solution.addTwoNumbers(l11, l21)
print(solution.toString(example))
