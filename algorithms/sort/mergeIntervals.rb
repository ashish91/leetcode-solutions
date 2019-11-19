class Solution:
  def merge(self, intervals: List[List[int]]) -> List[List[int]]:
    merged = []
    sorted_intervals = sorted(intervals, key=lambda i: i[0])

    for i in sorted_intervals:
      if merged and merged[-1][1] >= i[0]:
        merged[-1][1] = max(merged[-1][1], i[1])
      else:
        merged.append(i)

    return merged
