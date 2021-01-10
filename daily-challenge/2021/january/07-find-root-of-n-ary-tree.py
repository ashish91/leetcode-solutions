# Time complexity: O(N)
#   Each node is traversed twice
# Space complexity: O(1)
class Solution:
  def findRootOfNAryTree(self, adjlist, N):
    sum = 0

    for node in range(N):
      sum += node
      for child in adjlist[node]:
        # All non root nodes will be considered twice so
        # addition and subtraction will remove them.
        # While root is never a child so it'll be added
        # but not substracted. Finally root will remain
        sum -= child

    for node in range(N):
      if node == sum:
        return node

    return None

# Considering Overflow we can use XOR which have same property
class Solution:
  def findRootOfNAryTree(self, adjlist, N):
    sum = 0

    for node in range(N):
      sum ^= node
      for child in adjlist[node]:
        # All non root nodes will be considered twice so
        # Child ^ Child = None
        # While root is never a child so it'll be considered
        # once.
        sum ^= child

    for node in range(N):
      if node == sum:
        return node

    return None