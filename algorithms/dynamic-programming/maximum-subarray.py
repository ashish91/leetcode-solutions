class Solution:
  def maxSubArray(self, nums: List[int]) -> int:
    length = len(nums)
    cache = [0] * length

    cache[0] = nums[0]
    maxValue = nums[0]
    i = 1
    for i in range(1, length):
      cache[i] = max(cache[i-1] + nums[i], nums[i])

      if maxValue < cache[i]:
        maxValue = cache[i]

    return maxValue
