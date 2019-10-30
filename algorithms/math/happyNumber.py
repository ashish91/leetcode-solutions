class Solution:
  def digitSquareSum(self, n: int) -> int:
    sum = 0
    while n:
      tmp = n % 10
      sum += tmp * tmp
      n = int(n/10)
    return sum

  def isHappy(self, n: int) -> bool:
    slow = self.digitSquareSum(n)
    fast = self.digitSquareSum(n)
    fast = self.digitSquareSum(fast)

    while slow != fast:
      slow = self.digitSquareSum(slow)
      fast = self.digitSquareSum(fast)
      fast = self.digitSquareSum(fast)

    return slow == 1
