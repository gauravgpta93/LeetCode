class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows <= 1:
            return s
        single_bucket_size = (2 * numRows) - 2
        ans = [""] * numRows
        for index, value in enumerate(s):
            current_pos = index % single_bucket_size
            if current_pos < numRows:
                ans[current_pos] += value
            else:
                ans[single_bucket_size - current_pos] += value
        # print(ans)
        result = "".join(ans)
        return result
