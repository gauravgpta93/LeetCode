class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        sorted_list = sorted(heights)
        results = 0
        for index in range(len(heights)):
            if sorted_list[index] != heights[index]:
                results += 1
        return results
