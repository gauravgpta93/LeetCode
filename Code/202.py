class Solution:
    def isHappy(self, n: int) -> bool:
        marked_numbers = set()
        current = n
        while current not in marked_numbers:
            marked_numbers.add(current)
            current = self.get_square_sum_digits(current)
            if current == 1:
                return True
        return False

    def get_square_sum_digits(self, number):
        return sum([int(x) ** 2 for x in str(number)])
