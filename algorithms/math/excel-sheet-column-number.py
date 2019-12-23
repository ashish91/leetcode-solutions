class Solution:
  def titleToNumber(self, s: str) -> int:
    s = s[::-1]
    sum = 0
    for ind, c in enumerate(s):
        sum += (ord(c) - 65 + 1) * (26 ** ind)
    return sum
