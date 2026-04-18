class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        i = 0
        j = 1
        result = []
        while i < len(temperatures):
            if j >= len(temperatures):
                result.append(0)
                i += 1
                j = i + 1
                continue
            if j < len(temperatures) and temperatures[i] < temperatures[j]:
                    result.append(j - i)
                    m = 0
                    i += 1
                    j = i + 1
            else:
                j += 1
        
        return result

# brute force way : time: o(n^2) , space: o(n)