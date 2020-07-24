class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def _create(current, left, right):
            if len(current) == 2 * n:
                ans.append(current)
            else:
                if left < n:
                    _create(current + "(", left + 1, right)
                if right < left:
                    _create(current + ")", left, right + 1)

        ans = list()
        _create(str(), 0, 0)
        return ans