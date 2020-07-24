class Solution:
    def isPalindrome(self, x: int) -> bool:
        # return str(x) == str(x)[::-1]
        if x == 0:
            return True
        if x < 0 or x % 10 == 0:
            return False
        reverse_number = 0
        while x > reverse_number:
            reverse_number = (reverse_number * 10) + (x % 10)
            x = x // 10
        # print(reverse_number)
        return x == reverse_number or x == (reverse_number // 10)
