# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        curr = head
        visted = set()
    
        while curr:
            if curr.val not in visted:
                visted.add(curr.val)
            else:
                nxt = curr.next
                if nxt != None:
                    return True
            curr = curr.next
        return False
        