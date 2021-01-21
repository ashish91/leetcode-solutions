class Solution:
  def maximumGain(self, s: str, x: int, y: int) -> int:
    a = 'a'
    b = 'b'

    if x < y:
      a, b = b, a
      x, y = y, x
    seen = Counter()
    gain = 0

    for c in s+'x':
      if c == 'a' or c == 'b':
        if c == b and seen[a] > 0:
          gain += x
          seen[a] -= 1
        else:
          seen[c] += 1
      else:
        gain += y*min(seen[b], seen[a])
        seen[a], seen[b] = 0, 0

    return gain