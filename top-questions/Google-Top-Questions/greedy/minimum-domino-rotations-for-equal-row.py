class Solution:
  def minDominoRotations(self, A: List[int], B: List[int]) -> int:
    N = len(A)
    freq = {}
    possible = {}
    ans = None
    for i in range(N):
      if A[i] not in freq:
        freq[A[i]] = 0
      if B[i] not in freq:
        freq[B[i]] = 0

      if A[i] == B[i]:
        freq[A[i]] += 1
      else:
        freq[A[i]] += 1
        freq[B[i]] += 1

      if freq[A[i]] >= N:
        ans = A[i]
        break
      if freq[B[i]] >= N:
        ans = B[i]
        break

    if ans is None:
      return -1

    rotA = 0
    rotB = 0
    for i in range(N):
      if A[i] != B[i]:
        if A[i] == ans:
          rotA += 1
        elif B[i] == ans:
          rotB += 1

    return min(rotA, rotB)
