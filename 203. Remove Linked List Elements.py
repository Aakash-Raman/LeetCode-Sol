# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if not head:
            return head
        curr_node = head
        prev_node = head
        while curr_node:
            if curr_node.val == val:
                prev_node.next = curr_node.next
                if head.val == val:
                    head = head.next
            else:
                prev_node = curr_node
            curr_node = curr_node.next
        return head
