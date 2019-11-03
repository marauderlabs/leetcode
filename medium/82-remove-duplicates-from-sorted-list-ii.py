# https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        dummy = ListNode(None)
        newLast = dummy
        cur = head
        while cur:
            if cur.next and (cur.val == cur.next.val):
                while cur.next and cur.val == cur.next.val:
                    cur = cur.next
                cur = cur.next
            else:
                newLast.next = cur
                newLast = cur
                cur = cur.next
                newLast.next = None
        return dummy.next
