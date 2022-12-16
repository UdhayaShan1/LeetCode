# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if headA == headB:
            return headA
        length1 = 0
        length2 = 0
        curr1 = headA
        curr2 = headB
        while curr1:
            length1 += 1
            curr1 = curr1.next
        while curr2:
            length2 += 1
            curr2 = curr2.next
        if length1 >= length2:
            count = 0
            while count < (length1-length2):
                headA = headA.next
                count+=1
            
            flag = 0
            b1 = False
            
            a = ListNode(0,next=headA)
            b = ListNode(0,next=headB)
            
            curr = a
            curr1 = b
            while (b1==False):
                if curr.next == curr1.next:
                    return curr.next
                curr = curr.next
                curr1 = curr1.next
        else:
            count = 0
            while count < (abs(length1-length2)):
                headB = headB.next
                count+=1
            
            flag = 0
            b1 = False
            a = ListNode(0,next=headA)
            b = ListNode(0,next=headB)
            
            curr = a
            curr1 = b
            while (b1==False):
                if curr.next == curr1.next:
                    return curr.next
                curr = curr.next
                curr1 = curr1.next
