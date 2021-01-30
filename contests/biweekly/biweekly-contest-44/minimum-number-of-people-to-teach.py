class Solution:
  def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:
    # n = 2, languages = [[1],[2],[1,2]], friendships = [[1,2],[1,3],[2,3]]

    lang_lookup = {}
    for i,l in enumerate(languages):
      lang_lookup[i] = set(l)

    M = len(languages)
    can_comm = [[False for j in range(M)] for i in range(M)]
    for a,b in friendships:
      if lang_lookup[a-1] & lang_lookup[b-1]:
        can_comm[a-1][b-1] = True
        can_comm[b-1][a-1] = True

    ans = M
    for l in range(1,n+1):
      s = set()
      for a,b in friendships:
        a-=1
        b-=1

        if can_comm[a][b]:
          continue

        if l not in languages[a]:
          s.add(a)
        if l not in languages[b]:
          s.add(b)
      ans = min(ans,len(s))

    return ans