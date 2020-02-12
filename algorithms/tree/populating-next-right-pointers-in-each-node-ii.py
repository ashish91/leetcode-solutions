import collections

class Solution:
  def linkNextPointer(self, child, prev, curr, leftmost):
    if child:
      if prev:
        prev.next = child
      else:
        leftmost = child

      prev = child

    return leftmost, prev

  def connect(self, root: 'Node') -> 'Node':
    if root is None:
      return None

    leftmost = root

    while leftmost:

      prev, curr = None, leftmost
      leftmost = None

      while curr:
        leftmost, prev = self.linkNextPointer(curr.left, prev, curr, leftmost)
        leftmost, prev = self.linkNextPointer(curr.right, prev, curr, leftmost)

        curr = curr.next

    return root
