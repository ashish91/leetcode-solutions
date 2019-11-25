class Solution:
  def searchMatrix(self, matrix, target):
    """
    :type matrix: List[List[int]]
    :type target: int
    :rtype: bool
    """
    r = len(matrix)
    if r == 0:
      return False

    c = len(matrix[0])

    i = 0
    j = c - 1

    while i < r and j >= 0:
      if matrix[i][j] < target:
        i += 1
      elif matrix[i][j] > target:
        j -= 1
      else:
        return True

    return False
