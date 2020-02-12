class Solution:
  def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
    count_cache = [0] * 1001

    for num in arr1:
      count_cache[num] += 1

    i = 0
    for num in arr2:
      while count_cache[num] > 0:
        arr1[i] = num
        i += 1
        count_cache[num] -= 1

    index = 0
    for count in count_cache:
      while count > 0:
        arr1[i] = index
        i += 1
        count -= 1
      index += 1

    return arr1
