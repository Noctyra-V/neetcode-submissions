class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s = list(s)
        t = list(t)
        s.sort()
        t.sort()
        if s == t:
            return True
        return False
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for i in range(0,len(strs)):
                exist = any(strs[i] in lst for lst in anagrams.values())
                if exist:
                        continue
                anagrams[strs[i]] = []
                for j in range(i + 1,len(strs)):
                    if self.isAnagram(strs[i],strs[j]):
                        anagrams[strs[i]].append(strs[j])
        anagrams = [[k,*v] for k,v in anagrams.items()]
        return anagrams
            