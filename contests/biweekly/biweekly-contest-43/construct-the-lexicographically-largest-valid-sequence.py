class Solution:
  def constructDistancedSequence(self, n: int) -> List[int]:
    size = (2*n-1)
    arr = [0]*size
    seen = [False] * (n+1)

    def dfs(arr, i, seen):
      if i >= size:
        return True

      for a in range(n, 0, -1):
        if (a > 1 and ((not (arr[i] == 0 and (i+a < size) and arr[i+a] == 0)) or seen[a])) or (a == 1 and (arr[i] != 0 or seen[a])):
          continue

        if a > 1:
          arr[i] = a
          arr[i+a] = a
        else:
          arr[i] = a
        seen[a] = True

        next_ind = i+1
        while next_ind < size and arr[next_ind]:
          next_ind += 1

        if dfs(arr, next_ind, seen):
          return True

        if a > 1:
          arr[i] = 0
          arr[i+a] = 0
        else:
          arr[i] = 0
        seen[a] = False

      return False

    dfs(arr, 0, seen)
    return arr
