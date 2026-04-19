class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        i = 0
        nums = []
        while i < len(tokens):
            if  tokens[i] not in ('+','-','*','/'):
                nums.append(tokens[i])
                i += 1
            else:
                if tokens[i] == '+':
                    tokens[i] = int(nums.pop()) + int(nums.pop())
                    tokens.pop(i - 1)
                    tokens.pop(i - 2)
                elif tokens[i] == '-':
                    l = int(nums.pop()) 
                    bl = int(nums.pop()) 
                    tokens[i] = bl - l
                    tokens.pop(i - 1)
                    tokens.pop(i - 2)
                
                elif tokens[i] == '*':
                    tokens[i] = int(nums.pop()) *  int(nums.pop())
                    tokens.pop(i - 1)
                    tokens.pop(i - 2)
    
                elif tokens[i] == '/':
                    l = int(nums.pop()) 
                    bl = int(nums.pop()) 
                    tokens[i] = int(bl/l)
                    tokens.pop(i - 1)
                    tokens.pop(i - 2)
                i = i - 2
                
        return int(tokens[0])

# another solution : time:o(n), space:o(n)