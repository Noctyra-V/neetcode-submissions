class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        l = sorted(stones,reverse=True)
        while len(l) > 1:
            if l[0] == l[1]:
                l[0] = 0
                l[1] = 0
                l.remove(0)
            elif l[0] > l[1]:
                l[0] = l[0] - l[1]
                l[1] = 0
                l.remove(0)
            l = sorted([x for x in l if x != 0],reverse=True)
        if l == []:
            return 0
        return max(l)
         