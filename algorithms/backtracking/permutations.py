class Solution:
  def generate(self, nums: List[int], current_permutation: List[int], permutations: List[List[int]]) -> List[List[int]]:
    if len(nums) > 0:
      index = 0
      for num in nums:
        self.generate(nums[:index] + nums[index+1:], current_permutation + [ num ], permutations)
        index += 1
    else:
      permutations.append(current_permutation)

    return permutations

  def permute(self, nums: List[int]) -> List[List[int]]:
    current_permutation = []
    permutations = []

    self.generate(nums, current_permutation, permutations)
    return permutations
