# Using Sorting
# Time Complexity O(NlogN)
# Space Complexity O(1)
class Solution:
  def lastStoneWeight(self, stones: List[int]) -> int:
    stones.sort(reverse=True)
    while len(stones) > 1:
      arr = stones[2:]

      y = stones[0]
      x = stones[1]

      if x != y:
        arr.append(y-x)

      stones = sorted(arr,reverse=True)

    if stones:
      return stones[0]
    else:
      return 0

# Using Heap
# Time Complexity O(NlogN)
# Space Complexity O(NlogN)
import heapq as hq

class Solution:
  def lastStoneWeight(self, stones: List[int]) -> int:
    for i in range(len(stones)):
      stones[i] = -stones[i]
    heap = stones
    hq.heapify(heap)

    while len(heap) > 1:
      first = -1 * hq.heappop(heap)
      second = -1 * hq.heappop(heap)

      diff = first - second
      hq.heappush(heap, -diff)

    if len(heap) == 0:
      return 0
    else:
      return -heap[0]
