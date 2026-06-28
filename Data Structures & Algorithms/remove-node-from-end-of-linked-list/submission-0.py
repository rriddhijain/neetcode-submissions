# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr=head
        y=0
        if not head:
            return None
        
        while curr:
            curr=curr.next
            y+=1
        target=y-n
        v=0
        if target==0:
            return head.next
        temp=head
        while v!=target-1:
            temp=temp.next
            v+=1
        dele = temp.next
        temp.next=temp.next.next
        dele.next=None
        return head 



