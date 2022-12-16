# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        prev = None
        curr = slow
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
            
        flag = 0
        curr1 = head
        curr2 = prev
        while curr1 and curr2:
            if curr1.val != curr2.val:
                flag+=1
                break
            curr1 = curr1.next
            curr2 = curr2.next
        return flag == 0
            
