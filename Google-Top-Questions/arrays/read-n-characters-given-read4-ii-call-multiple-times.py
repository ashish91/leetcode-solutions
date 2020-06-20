# The read4 API is already defined for you.
# def read4(buf: List[str]) -> int:

class Solution:
  def __init__(self):
    self.buf = None

  def read(self, buf: List[str], n: int) -> int:
    totalrun = n//4
    remrun  = n % 4
    result  = []

    for i in range(totalrun):
      new_buf = ['']*4
      n_c = read4(new_buf)
      result.extend(new_buf[:n_c])
    if remrun >0:
      new_buf = ['']*4
      n_c =read4(new_buf)
      result.extend(new_buf[:n_c])

    if self.buf != None:
      if len(result) >0:
        result =  self.buf + result
      else:
        result =  self.buf

    buf[:] = result[:n]
    self.buf = result[n:]
    return len(buf)
