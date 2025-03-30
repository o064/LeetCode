# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        dummyHead =ListNode(0,head);
        first=dummyHead
        second =dummyHead

        for i in range(n+1):
            first = first.next
        while first :
            second = second.next
            first = first.next
        second.next = second.next.next
        return dummyHead.next

    
        