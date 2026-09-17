# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode | None, k: int) -> ListNode | None:
        
        if not head or not head.next or k == 0:
            return head

        l = 0
        curr = head
        while curr.next != None :
            curr = curr.next
            l += 1
        l += 1
        curr.next = head
        k = k % l

        if k == 0:
            curr.next = None
            return head
            
        curr = head

        for i in range(l - k - 1):
            curr = curr.next
        new_head = curr.next
        curr.next = None

        return new_head