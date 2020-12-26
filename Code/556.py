class Solution:
    def nextGreaterElement(self, n: int) -> int:
        n_list = list(str(n))
        i = len(n_list) - 1
        while i > 0 and n_list[i] <= n_list[i - 1]:
            i -= 1
        if i == 0:
            return -1

        j = i
        while j < len(n_list) and n_list[i - 1] < n_list[j]:
            j += 1

        n_list[i - 1], n_list[j - 1] = n_list[j - 1], n_list[i - 1]
        n_list[i:] = n_list[i:][::-1]
        ans = int("".join(n_list))
        return ans if ans < 1 << 31 else -1


if __name__ == '__main__':
    print(Solution().nextGreaterElement(234157641))
