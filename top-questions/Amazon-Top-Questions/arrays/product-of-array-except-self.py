class Solution:
  def productExceptSelf(self, nums: List[int]) -> List[int]:
    N = len(nums)

    product = [1 for i in range(N)]

    left = 1
    right = 1
    for i in range(1, N):
      left = left * nums[i-1]
      product[i] *= left

      right = right * nums[N-i]
      product[N-i-1] *= right

    return product