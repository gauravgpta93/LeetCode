class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        left, right = max(weights), sum(weights)

        while left < right:
            current = 0
            partitions = 1
            mid = (left + right)//2
            for weight in weights:
                if current + weight > mid:
                    current = 0
                    partitions += 1
                current += weight

            if partitions <= D:
                right = mid
            else:
                left = mid + 1
        return left
