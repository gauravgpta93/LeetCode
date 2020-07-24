class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            return 0
        max_int = (2 ** 31) - 1
        min_int = (-2 ** 31)
        string_rep = str(x)
        end = len(string_rep) - 1
        while string_rep[end] == "0":
            end -= 1
        string_rep = string_rep[end + 1::-1] if string_rep[0].isdigit() else string_rep[0] + string_rep[end + 1:0:-1]
        # print(string_rep)
        ans = int(string_rep)
        # print(ans)
        return ans if (min_int <= ans <= max_int) else 0


if __name__ == '__main__':
    print(Solution().reverse(0))
