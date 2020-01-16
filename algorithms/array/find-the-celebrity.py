# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
  def findCelebrity(self, n: int) -> int:
    celebrity = 0

    for someone in range(n):
      # celebrity doesn't know anybody,
      # so in end we'll reach possible celebrity.
      if knows(celebrity, someone):
        celebrity = someone

    for someone in range(celebrity):
      # Loop in graph.
      if knows(celebrity, someone):
        return -1

    for someone in range(n):
      # someone is disjoint from graph.
      if not knows(someone, celebrity):
        return -1

    return celebrity
