class Solution:
  def lengthOfLIS(self, nums: List[int]) -> int:
    n = len(nums)
    if n == 0:
      return 0

    mem = [1] * n

    i = n - 2
    lis = 1
    while i >= 0:
      j = i + 1
      while j < n:
        if nums[i] < nums[j]:
          mem[i] = max(mem[i], mem[j] + 1)
        j += 1
      lis = max(lis, mem[i])
      i -= 1

    return lis
