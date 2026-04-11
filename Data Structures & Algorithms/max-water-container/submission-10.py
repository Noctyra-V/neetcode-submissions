class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        m = float("-inf")
        j = len(heights) - 1
        while i < j:
            if min(heights[i],heights[j]) * len(heights[i:j]) > m:
                m = min(heights[i],heights[j]) * len(heights[i:j]) 
            if heights[i] > heights[j]:
                j -= 1
            elif heights[i] < heights[j]:
                i += 1
            else:
                i += 1
                j -= 1
        return m

# optimized way with a help