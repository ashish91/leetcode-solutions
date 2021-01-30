class Solution:
  def maximumBinaryString(self, binary: str) -> str:
    N = len(binary)

    first_zero = -1
    for i in range(N):
      if binary[i] == '0':
        if first_zero == -1:
          first_zero = i
        else:
          first_zero += 1

    if first_zero == -1:
      return binary

    ans = ''
    for i in range(N):
      if i == first_zero:
        ans += '0'
      else:
        ans += '1'

    return ans
