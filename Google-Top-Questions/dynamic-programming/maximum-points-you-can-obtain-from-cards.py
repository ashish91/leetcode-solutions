# Using DP with prefix sum
class Solution:
  def maxScore(self, p: List[int], k: int) -> int:
    N = len(p)
    left_sum = [0 for i in range(N+1)]
    right_sum = [0 for i in range(N+1)]

    for i in range(1, k+1):
      left_sum[i] += left_sum[i-1] + p[i-1]

    for i in range(1, k+1):
      right_sum[i] += right_sum[i-1] + p[N - i]

    ans = 0
    for i in range(k+1):
      ans = max(ans, left_sum[i] + right_sum[k-i])

    return ans

# Using Sliding Window
class Solution:
  def maxScore(self, p: List[int], k: int) -> int:
    N = len(p)

    start = 0
    curr_sum = 0
    min_sum = float('inf')
    total = 0

    size = N - k

    for end, val in enumerate(p):
      total += val
      curr_sum += val
      if end - start +1 > size:
        curr_sum -= p[start]
        start += 1

      if end-start+1 == size:
        min_sum = min(min_sum, curr_sum)

    return total - min_sum