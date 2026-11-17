# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # check which list head value is greater
        # set one start of the list to point to the other start of the list
        # then compare every in both list a continually build the new linked list

        cur_1, cur_2 = list1, list2
        # dummy node
        dummy = ListNode()
        tail = dummy

        while cur_1 != None and cur_2 != None:
            if cur_1.val < cur_2.val:
                tail.next = cur_1
                cur_1 = cur_1.next
            else:
                tail.next = cur_2
                cur_2 = cur_2.next

            tail = tail.next

        if cur_1:
            tail.next = cur_1

        elif cur_2:
            tail.next = cur_2

        return dummy.next
                

        

        
