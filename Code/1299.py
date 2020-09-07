class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        current_max = -1
        for index in range(len(arr)-1, -1, -1):
            temp, arr[index] = arr[index], current_max
            current_max = max(current_max, temp)
        return arr