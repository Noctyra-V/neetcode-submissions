class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        m = float("-inf")
        while i < len(heights) - 1:
            j = i
            while j < len(heights):
                m = max(m,min(heights[i],heights[j]) * len(heights[i:j]))
                j += 1
            i += 1
        return m
            