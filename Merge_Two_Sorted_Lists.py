# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        if list1 == None :
            return list2 

        if list2 == None :
            return list1 

        newnode = ListNode()
        if list1.val > list2.val:
            newnode.val = list2.val
            list2 = list2.next 
        else:
            newnode.val = list1.val
            list1 = list1.next 

        newnode.next = self.mergeTwoLists(list1 , list2 )
        return newnode 
