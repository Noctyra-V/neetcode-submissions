class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char = {}
        substring = ""
        m = 0
        i = 0
        j = len(s) - 1
        if len(s) == 1:
            return 1
        while i < len(s):
            j = len(s) - 1
            while i <= j:
                if s[j] not in char:
                    char[s[j]] = i
                    substring += s[j]
                else:
                    m = max(m,len(substring))
                    char = {} 
                    substring = ""
                j -= 1
            i += 1
        if substring:
            m = max(m,len(substring))
            return m
        return m
    

# Brute force way solution with complexity: time:o(n^2) and space:o(m) where m is the number of unique characters in the string

        
            