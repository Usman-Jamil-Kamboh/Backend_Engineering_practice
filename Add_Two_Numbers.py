# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        starting_node = ListNode()
        current = starting_node 
        carry = 0 
        digit = 0 
        while l1 or l2 or carry :
            value1 = l1.val if l1 else 0 
            value2 = l2.val if l2 else 0 
            digit = (value1 + value2 + carry ) % 10 
            carry = (value1 + value2 + carry ) // 10 

            current.next = ListNode(digit)
            current = current.next
            
            if l1 :
                l1 = l1.next
            if l2 :
                l2 = l2.next 
        return starting_node.next

            
