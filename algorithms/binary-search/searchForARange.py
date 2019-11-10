class Solution:

  def searchRange(self, nums: List[int], target: int) -> List[int]:
    result = [-1, -1]
    if len(nums) == 0:
      return result

    left = 0
    n = len(nums)
    right = n - 1

    while left < right:
      mid = int((left + right)/2)
      if nums[mid] < target:
        left = mid + 1
      else:
        right = mid

    if nums[left] != target:
      return result
    result[0] = left

    right = n - 1
    while left < right:
      mid = int((left + right)/2 + 1)
      if nums[mid] > target:
        right = mid - 1
      else:
        left = mid

    result[1] = right
    return result
