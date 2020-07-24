class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        if len(nums) < 3:
            return 0
        nums.sort()
        min_difference = None
        ans = 0
        for index in range(len(nums) - 2):
            if index > 0 and nums[index] == nums[index - 1]:
                continue
            left, right = index + 1, len(nums) - 1
            while left < right:
                local_difference = target - nums[index] - nums[left] - nums[right]
                if min_difference is None or abs(local_difference) < min_difference:
                    min_difference = abs(local_difference)
                    ans = nums[index] + nums[left] + nums[right]
                    if min_difference == 0:
                        return ans
                if local_difference < 0:
                    right -= 1
                else:
                    left += 1
        return ans
