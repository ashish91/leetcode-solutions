class Solution:
  def generate(self, nums, current_subset, all_subsets):
    all_subsets.append(current_subset)

    index = 0
    for num in nums:
      index += 1
      self.generate(nums[index:], current_subset + [num], all_subsets)

  def subsets(self, nums: List[int]) -> List[List[int]]:
    all_subsets = []

    self.generate(nums, [], all_subsets)
    return all_subsets
