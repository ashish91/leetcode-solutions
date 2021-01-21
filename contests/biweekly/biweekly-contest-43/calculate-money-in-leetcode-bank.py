class Solution:
  def totalMoney(self, n: int) -> int:
    if n <= 7:
      return n*(n+1)//2

    weeks = n//7
    # AP with 28 as starting with 7 as diff
    # Week 1 => Money 28
    # Week 2 => Money 28+7
    # Week 3 => Money 28+7
    # Week 4 => Money 28+7
    money = (weeks * ((2*28) + (weeks - 1)*7))//2

    if n % 7 > 0:
      days = n % 7
      day = weeks+1
      for j in range(days):
        money += day
        day += 1

    return money