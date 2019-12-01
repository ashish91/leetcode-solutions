class Solution:
  def coinChange(self, coins: List[int], amount: int) -> int:
    if amount == 0:
      return 0

    mem = [float('inf')] * (amount + 1)
    mem[0] = 0

    for coin in coins:
      for i in range(coin, amount + 1):
        mem[i] = min(mem[i], mem[i - coin] + 1)

    if mem[-1] == float('inf'):
      return -1
    else:
      return mem[-1]
