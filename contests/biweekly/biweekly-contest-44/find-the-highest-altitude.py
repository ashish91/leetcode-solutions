class Solution:
  def largestAltitude(self, gain: List[int]) -> int:
    ans = 0
    sum = 0
    for g in gain:
      sum += g
      ans = max(ans, sum)

    return ans
