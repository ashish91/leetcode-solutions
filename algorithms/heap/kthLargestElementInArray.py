from heapq import *

class Solution:
  def findKthLargest(self, nums: List[int], k: int) -> int:
    maxheap = []
    l = len(nums) - k + 1

    for num in nums:
      heappush(maxheap, -1 * num)
      if len(maxheap) > l:
        heappop(maxheap)

    return -1 * heappop(maxheap)
