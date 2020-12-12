class Solution:
  def reorganizeString(self, S):
    more_than_half = False
    count = collections.Counter()
    N = len(S)

    for c in S:
      count[c] += 1
      if count[c] > (N + 1)/2:
        more_than_half = True

    if more_than_half:
      return ""

    heap = []
    for c in count.keys():
      heap.append([-1*count[c], c])
    heapq.heapify(heap)

    ans = []
    while len(heap) >= 2:
      ct1, c1 = heapq.heappop(heap)
      ct2, c2 = heapq.heappop(heap)

      ans.extend([c1, c2])
      if ct1 + 1: heapq.heappush(heap, [ct1 + 1, c1])
      if ct2 + 1: heapq.heappush(heap, [ct2 + 1, c2])

    return "".join(ans) + (heap[0][1] if heap else '')