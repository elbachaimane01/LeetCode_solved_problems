# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        
        unique=[]
        Current=head
        output=None
        
        while Current!= None:
            if Current.val not in unique:
                unique.append(Current.val)
            Current=Current.next
    
        for i in reversed(unique):
            output=ListNode(i,output)
        
        return output


        