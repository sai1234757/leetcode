# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, data=0, next=None):
#         self.data = data
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        d=ListNode(0)
        d.next=head
        prev=d
        curr=head
        while curr:
            n=curr.next
            if n is not None and n.val==curr.val:
                while n is not None and n.val==curr.val:
                    n=n.next
                prev.next=n
                current =n
            else:
                prev=curr
                curr=curr.next
        return d.next