class Solution:
    def spiralMatrixIII(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
        i, j = r0, c0
        size_ring = 1
        direction = 1  # 1 for left, down. -1 for other 2
        ans = [(r0, c0)]
        while len(ans) < R * C:
            for _ in range(size_ring):
                j += direction
                if 0 <= i < R and 0 <= j < C:
                    ans.append((i, j))
            for _ in range(size_ring):
                i += direction
                if 0 <= i < R and 0 <= j < C:
                    ans.append((i, j))

            size_ring += 1
            direction *= -1
        return ans