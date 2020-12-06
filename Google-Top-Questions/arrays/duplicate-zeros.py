class Solution:
  def duplicateZeros(self, arr: List[int]) -> None:
    """
    Do not return anything, modify arr in-place instead.
    """

    N = len(arr)
    zeroes = 0

    for i in range(N):
      if i > N - 1 - zeroes:
        break

      if arr[i] == 0:
        if i == N - 1 - zeroes:
          arr[N-1] = 0
          N -= 1
          break

        zeroes += 1

    new_last = N - 1 - zeroes

    for i in range(new_last, -1, -1):
      if arr[i] == 0:
        arr[i+zeroes] = 0
        zeroes -= 1
        arr[i+zeroes] = 0
      else:
        arr[i+zeroes] = arr[i]