class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0]*len(temperatures)
        for i,t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                
                stackt , stackid = stack.pop()
                res[stackid] = i - stackid
                
            stack.append((t,i))
        return res



# solution optimized with help of the video and explanation of decreasing monotonic stack:
# time:o(n) and space:o(n)

