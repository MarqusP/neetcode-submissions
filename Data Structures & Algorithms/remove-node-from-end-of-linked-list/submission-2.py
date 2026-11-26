# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # create dummy node
        dummy = ListNode()
        dummy.next = head

        l, r = dummy, head

        # create r pointer and move forward from the head n times
        while n != 0:
            r = r.next
            n -= 1
        
        # move both pointers by one
        while r:
            l = l.next
            r = r.next
            
            # r is null
            if not r:
                break
        
        nxt = l.next.next
        l.next = nxt

        return dummy.next
                
            

        

