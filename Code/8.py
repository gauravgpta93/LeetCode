class Solution:
    def myAtoi(self, str: str) -> int:
        ans = ""
        started = False
        sign = "+"
        for x in str:
            if started and not x.isdigit():
                break
            elif x == "+" or x == "-":
                started = True
                sign = x
            elif x.isdigit():
                started = True
                ans += x
            elif x == " ":
                continue
            else:
                break
        ans = sign + ans if ans else 0
        ans = int(ans) if ans else 0
        min_int = -2 ** 31
        max_int = (2 ** 31) - 1
        if sign == "+":
            return min(max_int, ans)
        else:
            return max(min_int, ans)
