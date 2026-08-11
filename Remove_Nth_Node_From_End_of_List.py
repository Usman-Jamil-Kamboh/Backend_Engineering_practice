# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        dummy = ListNode()
        dummy.next = head
        
        i = 0
        slow = dummy
        fast = dummy

        while fast.next is not None :   
            fast = fast.next 
            i += 1
            if i > n :
                slow = slow.next

        slow.next = slow.next.next
        return dummy.next

        

