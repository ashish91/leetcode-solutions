class Solution:
  def maxSubArray(self, nums: List[int]) -> int:
    size = len(nums)
    dp = [0] * size
    i = 1
    dp[0] = nums[0]
    result = nums[0]

    while i < size:
      dp[i] = nums[i]
      if dp[i - 1] > 0:
        dp[i] = dp[i] + dp[i-1]

      result = max(result, dp[i])
      i += 1

    return result
