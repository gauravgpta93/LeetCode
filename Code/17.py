class Solution:
    def __init__(self):
        self.result = list()
        self.phone_dict = {'2': ['a', 'b', 'c'],
                           '3': ['d', 'e', 'f'],
                           '4': ['g', 'h', 'i'],
                           '5': ['j', 'k', 'l'],
                           '6': ['m', 'n', 'o'],
                           '7': ['p', 'q', 'r', 's'],
                           '8': ['t', 'u', 'v'],
                           '9': ['w', 'x', 'y', 'z']}

    def letterCombinations(self, digits: str) -> List[str]:
        if not len(digits):
            return []
        self._get_combination("", digits)
        return self.result

    def _get_combination(self, string, next_digits):
        if not len(next_digits):
            self.result.append(string)
        else:
            if next_digits[0] in self.phone_dict:
                result = list()
                for value in self.phone_dict[next_digits[0]]:
                    self._get_combination(string + value, next_digits[1:])
