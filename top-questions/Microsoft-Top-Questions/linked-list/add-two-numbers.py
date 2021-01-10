# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
  def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
    dummy = ListNode(0)
    carry, curr = 0, dummy
    p, q = l1, l2

    while p != None or q != None:
      x = p.val if (p is not None) else 0
      y = q.val if (q is not None) else 0

      sum = carry + x + y
      carry = int(sum/10)

      curr.next = ListNode(sum%10)
      curr = curr.next

      if p is not None: p = p.next
      if q is not None: q = q.next

    if carry > 0:
      curr.next = ListNode(carry)
    return dummy.next
