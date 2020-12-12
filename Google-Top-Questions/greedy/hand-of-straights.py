class Solution:
  def isNStraightHand(self, hand: List[int], W: int) -> bool:
    count = collections.Counter(hand)

    for c in sorted(count):
      if count[c] > 0:
        for v in range(W,-1,-1):
          count[c+v-1] -= count[c]
          if count[c+v-1] < 0:
            return False
    return True
