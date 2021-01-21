# Bottom up buildup of solutions using DFS + Backtracking
class Solution:
  def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
    N = len(graph)
    def dfs(curr, graph):
      nonlocal N

      if curr == N-1:
        return [[N-1]]

      partial = []
      for nei in graph[curr]:
        paths = dfs(nei, graph)
        for p in paths:
          partial.append([curr]+p)

      return partial

    return dfs(0, graph)

# Top Down buildup of solutions using DFS + Backtracking
class Solution:
  def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
    N = len(graph)
    ans = []
    def dfs(curr, path, graph):
      nonlocal N, ans

      if curr == N-1:
        ans.append(path)

      for nei in graph[curr]:
        dfs(nei, path+[nei], graph)


    dfs(0, [0], graph)
    return ans
