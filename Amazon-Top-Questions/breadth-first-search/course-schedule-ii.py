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