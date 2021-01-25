class Solution:
  def decode(self, encoded: List[int]) -> List[int]:
    all = 0
    excluding_first = 0
    n = len(encoded)

    for i in range(n):
      all ^= i+1
      if i%2 != 0:
        excluding_first ^= encoded[i]

    all ^= (n+1)
    first = all ^ excluding_first
    ans = [first]
    for v in encoded:
      next = ans[-1] ^v
      ans.append(next)

    return ans
