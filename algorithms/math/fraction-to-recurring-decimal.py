class Solution:
  def fractionToDecimal(self, numerator: int, denominator: int) -> str:
    if numerator == 0:
      return '0'

    if bool(numerator < 0) ^ bool(denominator < 0):
      fraction = '-'
    else:
      fraction = ''

    dividend = abs(numerator)
    divisor = abs(denominator)

    fraction += str(int(dividend/divisor))
    dividend = dividend%divisor

    if dividend == 0:
      return fraction

    fraction += '.'
    map = {}

    map[dividend] = len(fraction)
    while dividend != 0:
      dividend *= 10
      fraction += str(int(dividend/divisor))
      dividend = dividend%divisor

      if dividend in map:
        # do something
        index = map[dividend]
        fraction = fraction[:index] + '(' + fraction[index:] + ')'
        print(dividend)
        break
      else:
        map[dividend] = len(fraction)

    return fraction
