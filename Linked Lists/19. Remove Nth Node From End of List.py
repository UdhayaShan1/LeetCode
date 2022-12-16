# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        curr = head
        while curr:
            length+=1
            curr = curr.next
        
        new = ListNode(next=head)
        curr2 = new
        count = 0
        b1 = False
        while b1 == False:
            if count == length-n:
                curr2.next = curr2.next.next
                break
            curr2 = curr2.next
            count+=1
        return new.next
            
