class Solution:
  def twoSum(self, nums: List[int], target: int) -> List[int]:
    cache = {}
    i = 0
    for num in nums:
      if (target - num) in cache:
        return sorted([ cache[target - num], i ])

      cache[num] = i
      i += 1
