# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None :
            return head
        if head.next == None:
            return head

        privious = None 
        current = head
        afterCurrent = None 

        while current != None :
            afterCurrent = current.next
            current.next = privious
            privious = current 
            current = afterCurrent 
            
        head = privious 
        return head
        
