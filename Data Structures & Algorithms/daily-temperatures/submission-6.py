class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = []
        val = 0
        temp = temperatures
        i = 0

        for j in range(len(temp)):
            stack.append((temp[j],j))
        old = stack.copy()
        print(stack)

        while i < len(temp):
            if not stack:
                stack = old.copy()
                print(stack)
                res.append(val)
                val = 0
                i += 1
                continue
            
            if stack:
                if temp[i] < stack[-1][0] and stack[-1][1] > i:
                    val  = stack[-1][1] - i
                stack.pop()
                    
        
      
        return res

