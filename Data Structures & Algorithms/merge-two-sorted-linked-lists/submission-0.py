# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode(0)
        trail=dummy
        curr1=list1
        curr2=list2
        while curr1 and curr2:
            if curr1.val<=curr2.val:
                trail.next=curr1
                curr1=curr1.next
                trail=trail.next
            elif curr1.val>curr2.val:
                trail.next=curr2
                curr2=curr2.next
                trail=trail.next
        if not curr2 and curr1:
            trail.next=curr1
            trail=trail.next
        elif not curr1 and curr2:
            trail.next=curr2
            trail=trail.next
        return dummy.next
            
