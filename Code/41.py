class Solution:
    def firstMissingPositive(self, nums):
        l, r = 0, len(nums) - 1
        while l < r:
            if nums[l] < 0:
                nums[l], nums[r] = nums[r], nums[l]
                r -= 1
            else:
                l += 1
        start = 0


if __name__ == '__main__':
    Solution().firstMissingPositive([1, -2, 3, 4, 12, 0, -5])
