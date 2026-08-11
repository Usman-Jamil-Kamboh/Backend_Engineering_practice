# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.

        """

        if head is None or head.next is None:
            return
        
        slow = head 
        fast = head 

        while fast is not None and fast.next is not None :
            slow = slow.next 
            fast = fast.next.next 

        second_half = slow.next 
        slow.next = None 

        privious = None 
        current = second_half 
        after_current = None 

        while current is not None :
            after_current = current.next 
            current.next = privious 
            privious = current 
            current = after_current
        second_half = privious

        while head is not None and second_half is not None :
            head_second_node = head.next 
            second_half_second_node = second_half.next 
            head.next = second_half 
            second_half.next = head_second_node
            head = head_second_node 
            second_half = second_half_second_node
        


        
        
