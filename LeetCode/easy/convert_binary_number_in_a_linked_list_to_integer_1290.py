"""
1290. Convert Binary Number in a Linked List to Integer
https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/
"""


class Solution:
    def getDecimalValue(self, head):
        result_str = ""
        node = head
        while True:
            result_str += str(node.val)
            if not node.next:
                break
            node = node.next
        return int(result_str, 2)
