# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        curr, prev, temp, nxt = head, None, None, None

        # keep track of the curr, nxt, last
        while curr.next:
            nxt = curr.next
            temp = curr
            if curr.next.next == None:
                break
            while temp.next.next != None:
                temp = temp.next
            temp_prev = temp
            temp = temp.next
            temp_prev.next = None
            curr.next = temp                
            curr.next.next = nxt

            curr = curr.next.next



        
                    