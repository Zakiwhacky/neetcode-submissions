# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        curr = head
        l = curr
        r = curr
        if not r.next:
                return False
        while r.next and r:
            l = l.next
            r = r.next.next
            if l == r:
                return True
            if not r:
                return False
        return False