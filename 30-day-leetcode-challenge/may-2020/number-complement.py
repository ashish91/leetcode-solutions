class Solution:
  def findComplement(self, num: int) -> int:
    one = (1 << num.bit_length())
    shifted = one - 1
    return shifted ^ num
