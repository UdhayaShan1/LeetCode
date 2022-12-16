# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        str1 = ""
        str2 = ""
        head1 = l1;
        head2 = l2;
        length1 = 0
        length2 = 0
        while head1:
            str1 += str(head1.val)
            head1 = head1.next
            length1 += 1
        while head2:
            str2 += str(head2.val)
            head2 = head2.next
            length2 += 1
        str1 = str1[::-1]
        str2 = str2[::-1]
        
        sum1 = str(int(str1)+int(str2))
        sum1 = sum1[::-1]
        len1 = len(str(sum1))
        
        dummy = ListNode(0)
        curr = dummy
        count = 0;
        b1 = False
        while b1==False:
            if count == len1:
                break
            new = ListNode(int(str(sum1)[count]))
            curr.next = new
            curr = new
            count+=1
        return dummy.next
        
        
