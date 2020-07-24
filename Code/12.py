class Solution:
    def intToRoman(self, num: int) -> str:
        strs = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
        nums = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        ans = str()
        for index, value in enumerate(nums):
            while num >= value:
                ans += strs[index]
                num -= value
            if num == 0:
                return ans
