import heapq

class Solution:
  def minMeetingRooms(self, intervals: List[List[int]]) -> int:
    if not intervals:
      return 0

    intervals.sort()

    conferences = []
    heapq.heappush(conferences, intervals[0][1])

    for interval in intervals[1:]:
      if conferences[0] <= interval[0]:
        heapq.heappop(conferences)

      heapq.heappush(conferences, interval[1])

    return len(conferences)
