# Backtracking solution
# Time Complexity: O(5^N)
# Space Complexity: O(N)
class Solution:
  def countVowelStrings(self, n: int) -> int:
    vowels = ['a', 'e', 'i', 'o','u']
    ans = 0

    def dfs(curr):
      nonlocal n, ans

      if len(curr) == n:
        ans += 1
        return

      for c in vowels:
        if len(curr) == 0 or curr[-1] <=  c:
          dfs(curr+c)

    dfs('')
    return ans

# Push Down Bottom Up DP
# Time Complexity: O(Nk)
# Space Complexity: O(k)
class Solution:
  def countVowelStrings(self, n: int) -> int:
    k = 5
    if n == 1:
      return k

    dp = [1] * k
    for i in range(n):
      sum = 0
      for j in range(4, -1, -1):
        dp[j] += sum
        sum = dp[j]

    return dp[0]
