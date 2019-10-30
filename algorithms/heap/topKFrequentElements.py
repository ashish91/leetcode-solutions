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
