"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        mapping = {}

        temp = head 

        dummy_node = Node(0) 
        copy_temp = dummy_node
        
        while temp is not None : 
            newnode = Node(temp.val)
            mapping[temp] = newnode 
            copy_temp.next = newnode 
            copy_temp = newnode
            temp = temp.next 

        copy_head = dummy_node.next

        temp = head 
        copy_temp = copy_head
        while temp is not None :
            if temp.random is None:
                copy_temp.random = None
            else:
                copy_temp.random = mapping[temp.random]
            
            temp = temp.next
            copy_temp = copy_temp.next
    
        return copy_head
        


        
