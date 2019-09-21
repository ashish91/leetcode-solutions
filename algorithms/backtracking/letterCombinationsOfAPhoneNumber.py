class Solution:
  def letterCombinations(self, digits: str) -> List[str]:
    code = {
      '1': '',
      '2': 'abc',
      '3': 'def',
      '4': 'ghi',
      '5': 'jkl',
      '6': 'mno',
      '7': 'pqrs',
      '8': 'tuv',
      '9': 'wxyz',
      '0': ' '
    }
    combinations = [''] if digits else []

    for digit in digits:
      current_combinations = []
      for letter in code[digit]:
        for combination in combinations:
          current_combinations.append(combination + letter)
      combinations = current_combinations

    return combinations
