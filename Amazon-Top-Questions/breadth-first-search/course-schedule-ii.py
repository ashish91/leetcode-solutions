## Using topological sorting
class Solution:
  def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
    graph = defaultdict(list)

    for src, dest in prerequisites:
      graph[src].append(dest)

    color = { c: 0 for c in range(numCourses) }
    has_loop = False
    topological_order = []
    def dfs(node):
      nonlocal has_loop

      if has_loop:
        return

      color[node] = True
      for neighbour in graph[node]:
        if color[neighbour] == 0:
          dfs(neighbour)
        elif color[neighbour] == 1:
          has_loop = True

      color[node] = 2
      topological_order.append(node)

    for v in range(numCourses):
      if not has_loop and color[v] == 0:
        dfs(v)

    return topological_order if not has_loop else []

## Using indegree computation
from collections import defaultdict, deque
class Solution:
  def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
    adj_list = defaultdict(list)
    indeg = {}

    for dest, src in prerequisites:
      adj_list[src].append(dest)
      indeg[dest] = indeg.get(dest, 0) + 1

    print(adj_list)
    zero_indeg = deque([v for v in range(numCourses) if v not in indeg])
    print(zero_indeg)

    topological_order = []
    while len(zero_indeg) > 0:
      v = zero_indeg.popleft()
      topological_order.append(v)

      if v in adj_list:
        for neighbour in adj_list[v]:
          indeg[neighbour] -= 1
          if indeg[neighbour] == 0:
            zero_indeg.append(neighbour)

    return topological_order if len(topological_order) == numCourses else []