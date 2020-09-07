class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        m1 = m2 = m3 = -float("inf")
        for num in nums:
            if num in [m1, m2, m3]:
                continue
            if num > m1:
                m1, m2, m3 = num, m1, m2
            elif num > m2:
                m1, m2, m3 = m1, num, m2
            elif num > m3:
                m1, m2, m3 = m1, m2, num
        return m3 if m3 != -float("inf") else m1
