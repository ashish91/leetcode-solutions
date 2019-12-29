class Vector2D:

  def __init__(self, v: List[List[int]]):
    self.vector = v
    self.r = 0
    self.c = 0

    self.adjustForColumn()

  def next(self) -> int:
    if self.hasNext():
      item = self.vector[self.r][self.c]
      self.c += 1
      self.adjustForColumn()
      return item

  def hasNext(self) -> bool:
    return self.r < len(self.vector)

  def adjustForColumn(self):
    while self.r < len(self.vector) and self.c >= len(self.vector[self.r]):
      self.c = 0
      self.r += 1
