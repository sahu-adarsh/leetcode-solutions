# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        prv, cur = dummy, dummy.next
        counter = 0

        while cur:
            a = prv
            prv = cur
            cur = cur.next
            
            if cur:
                b = prv
                nxt = cur.next
                cur.next = prv
                prv = cur
                cur = nxt

                a.next = prv
                b.next = cur
                prv = b

        return dummy.next