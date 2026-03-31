class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        k = len(heights) - 1
        output = 0
        while i < k:
            output = max(output,min(heights[i],heights[k])*(k-i))
            if heights[k] > heights[i]:
                i += 1
            else:
                k -= 1
        return output
            