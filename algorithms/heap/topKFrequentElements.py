# Without heap
class Solution:
  def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    freq_hash = {}
    for num in nums:
      if num in freq_hash:
        freq_hash[num] += 1
      else:
        freq_hash[num] = 1

    freq = [0] * len(freq_hash)
    j = 0
    for num in freq_hash.keys():
      freq[j] = [num, freq_hash[num]]
      j += 1

    # Sort according to the elements
    freq = sorted(freq, key = lambda x : x[0], reverse = True)
    # Sort according to the frequency
    freq = sorted(freq, key = lambda x : x[1], reverse = True)

    top_k = [0] * k
    for i in range(k):
      top_k[i] = freq[i][0]

    return top_k

# With heap
from heapq import *

class Solution:
  def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    frequencies = {}
    for num in nums:
      if num in frequencies:
        frequencies[num] += 1
      else:
        frequencies[num] = 1

    values = {}
    for val in frequencies.keys():
      if frequencies[val] in values:
        values[frequencies[val]].append(val)
      else:
        values[frequencies[val]] = [val]

    heap = []
    for freq in values.keys():
      heappush(heap, freq * -1)
      print(heap)
      print(len(heap))

    top_k = []
    i = 0
    while i < k:
      freq = -1 * heappop(heap)
      i += len(values[freq])

      for val in values[freq]:
        top_k.append(val)

    return top_k
