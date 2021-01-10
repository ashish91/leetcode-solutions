# Using Heap
# O(NlogK)
class Solution:
  def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
    heap = []

    for (x, y) in points:
      dist = -(x*x + y*y)
      if len(heap) == K:
        heapq.heappushpop(heap, (dist, x, y))
      else:
        heapq.heappush(heap, (dist, x, y))

    return [(x,y) for (dist,x, y) in heap]

# Using quick select
# Avg case O(N), Worst O(N^2)
class Solution:
  def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
    length = len(points)
    l = 0
    r = length - 1

    while l <= r:
    	mid = self.qSelect(points, l, r)
    	if mid == K:
    		break
    	elif mid > K:
    		r = mid - 1
    	else:
    		l = mid + 1

    return points[0:K]

  def qSelect(self, arr, l, r):
  	pivot = arr[l]

  	while l < r:
  		# If r is greater than pivot then it's at the right position w.r.t. pivot
  		# So decrement r since r is at the right position
  		while l < r and self.compare(arr[r], pivot) >= 0: r-=1
  		# If r is smaller than pivot then move it to the left of the pivot
  		arr[l] = arr[r]

  		# If l is smaller than pivot then it's at the left position w.r.t. pivot
  		# So increment l since l is at the correct position
  		while l < r and self.compare(arr[l], pivot) <= 0: l+=1
  		# If l is greater than pivot then move it to the right of the pivot
  		arr[r] = arr[l]

  	# when l == r the loop will end. This is also the mid position w.r.t l and r
  	# so pivot should be placed at this position
  	arr[l] = pivot

  	return l

  def compare(self, p1, p2):
    return p1[0] * p1[0] + p1[1] * p1[1] - p2[0] * p2[0] - p2[1] * p2[1]