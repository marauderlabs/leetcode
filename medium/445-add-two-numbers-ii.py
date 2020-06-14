# https://leetcode.com/problems/add-two-numbers-ii/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        n1 = []
        n2 = []
        
        while l1:
            n1.append(l1.val)
            l1 = l1.next
        
        while l2:
            n2.append(l2.val)
            l2 = l2.next
        
        l3 = None
        carry = 0
        
        while n1 or n2:
            first = n1.pop() if n1 else 0 
            second = n2.pop() if n2 else 0
            add = first + second + carry
            
            l3 = ListNode(val=add%10, next=l3)
            carry = add // 10

        if carry:
            l3 = ListNode(val=carry, next=l3)
            
        return l3
            
