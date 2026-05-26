# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        prv, cur = dummy, dummy.next
        counter = 0

        def valid(p, c):
            a, b = p, c
            ln = 0
            while b:
                ln += 1
                if ln == k-1:
                    return True
                a = b 
                b = b.next

            return False


        while cur:
            a = prv
            prv = cur
            cur = cur.next
            
            if not valid(prv, cur):
                break

            if cur:
                b = prv
                for _ in range(k-1):
                    nxt = cur.next
                    cur.next = prv
                    prv = cur
                    cur = nxt

                a.next = prv
                b.next = cur
                prv = b

        return dummy.next