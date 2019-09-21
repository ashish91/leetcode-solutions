class Solution:
  def generate(self, p: int, left: int, right: int, result: List[str]):
    if left > right:
      return
    if left == 0 and right == 0:
      result.append(p)

    if left > 0:
      self.generate(p + '(', left-1, right, result)
    if right > 0:
      self.generate(p + ')', left, right-1, result)

    return

  def generateParenthesis(self, n: int) -> List[str]:
    if not n:
      return []

    result = []
    self.generate('', n, n, result)
    return result
