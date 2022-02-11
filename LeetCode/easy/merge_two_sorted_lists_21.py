"""
21. Merge Two Sorted Lists
https://leetcode.com/problems/merge-two-sorted-lists/
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def __init__(self):
        self.head = ListNode()

    def mergeTwoLists(self, a, b):
        a_list = []
        if a:
            while True:
                a_list += [a.val]
                if not a.next:
                    break
                else:
                    a = a.next

        b_list = []
        if b:
            while True:
                b_list += [b.val]
                if not b.next:
                    break
                else:
                    b = b.next

        result_list = sorted(a_list + b_list)
        i = len(result_list) - 1
        while i >= 0:
            current_node = ListNode()
            current_node.val = result_list[i]
            if i == len(result_list) - 1:
                current_node.next = None
            else:
                current_node.next = previous_node
            previous_node = current_node
            i -= 1
        return current_node if current_node else ListNode(0).next


list1_3 = ListNode(4)
list1_2 = ListNode(2, list1_3)
list1_1 = ListNode(1, list1_2)

list2_3 = ListNode(4)
list2_2 = ListNode(3, list2_3)
list2_1 = ListNode(1, list2_2)

sol = Solution()
head = sol.mergeTwoLists(list1_1, list2_1)
print(head.val, head.next.val)
