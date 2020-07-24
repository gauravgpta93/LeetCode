class Solution:
    def threeSum(self, nums):
        nums.sort()
        # print(nums)
        ans = list()
        for index in range(len(nums) - 2):
            if index > 0 and nums[index] == nums[index - 1]:
                continue
            left = index + 1
            right = len(nums) - 1
            while left < right:
                current_sum = nums[left] + nums[right] + nums[index]
                if current_sum == 0:
                    ans.append([nums[index], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif current_sum < 0:
                    left += 1
                else:
                    right -= 1
        return ans
