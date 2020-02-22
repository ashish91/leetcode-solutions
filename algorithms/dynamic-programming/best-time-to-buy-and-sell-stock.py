class Solution:
  def maxProfit(self, prices: List[int]) -> int:
    length = len(prices)
    if length <= 1:
      return 0

    left_view = [0] * length
    right_view = [0] * length

    left_view[0] = prices[0]
    for i in range(1, length):
      left_view[i] = min(left_view[i-1], prices[i])

    right_view[length - 1] = prices[length - 1]
    for i in reversed(range(length - 1)):
      right_view[i] = max(right_view[i+1], prices[i])

    profit = 0
    for i in range(length):
      if right_view[i] - left_view[i] > profit:
        profit = right_view[i] - left_view[i]

    return profit
