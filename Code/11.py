class Solution:
    def maxArea(self, height: List[int]) -> int:
        start, end = 0, len(height) - 1
        max_capacity = 0
        while start < end:
            start_height = height[start]
            end_height = height[end]
            current_capacity = min(start_height, end_height) * (end - start)
            max_capacity = max(current_capacity, max_capacity)
            if start_height <= end_height:
                start += 1
            else:
                end -= 1
        return max_capacity
