class Solution:
  def search(self, nums: List[int], target: int) -> int:
    N = len(nums)

    if N == 0:
      return -1

    left = 0
    right = N - 1

    while left < right:
      mid = int((left + right)/2)
      if nums[mid] > nums[right]:
        left = mid + 1
      else:
        right = mid

    rotation = left
    left = 0
    right = N - 1

    while left <= right:
      mid = int((left + right)/2)
      rotated_mid = (mid + rotation)%N

      if nums[rotated_mid] == target:
        return rotated_mid
      if nums[rotated_mid] < target:
        left = mid + 1
      else:
        right = mid - 1

    return -1
