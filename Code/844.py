class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        return self.get_string(S) == self.get_string(T)

    def get_string(self, s):
        ans = list()
        for l in s:
            if l == "#":
                if ans:
                    ans.pop()
            else:
                ans.append(l)
        return "".join(ans)
