# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[Optional[ListNode]]
        :rtype: Optional[ListNode]
        """
        def merge(left , right):
            dummyHead = merged
            while left and right : 
                if left.val <= right.val:
                    dummyHead.next = left 
                    dummyHead = dummyHead.next
                    left = left.next
                else :
                    dummyHead.next = right 
                    dummyHead = dummyHead.next
                    right = right.next
            while left : 
                    dummyHead.next = left 
                    dummyHead = dummyHead.next
                    left = left.next
            while right :
                    dummyHead.next = right 
                    dummyHead = dummyHead.next
                    right = right.next
        while len(lists)  > 1:
            right = lists.pop()
            left = lists.pop()
            merged = ListNode()
            merge(left,right)
            merged = merged.next
            lists.append(merged)
        return lists[0] if lists else None

