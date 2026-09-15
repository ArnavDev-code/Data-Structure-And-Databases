# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        prev = None
        current = head

        while current != None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        rev_head = prev

        if n == 1:
            rev_head = rev_head.next
        else:
            current = rev_head
            for i in range(n-2):
                current = current.next

            current.next = current.next.next

        prev = None
        current = rev_head

        while current is not None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        return prev
