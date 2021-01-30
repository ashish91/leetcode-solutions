class Solution:
  def averageWaitingTime(self, customers: List[List[int]]) -> float:
    N = len(customers)

    curr_time = customers[0][0]
    total_wait = 0
    for i in range(N):
      curr_time = max(curr_time, customers[i][0])

      total_wait += customers[i][1]
      curr_time += customers[i][1]

      if i+1 < N:
        total_wait += max(curr_time - customers[i+1][0], 0)

    return total_wait/N