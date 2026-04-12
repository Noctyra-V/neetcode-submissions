class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        i = 0
        l = sorted(nums)
        j = len(nums) - 1
        res = []
        while i < len(nums) - 1:
                k = i + 1
                j = len(nums) - 1
                while j > k:
                    c = sorted([l[i], l[j], l[k]])
                    if l[j] + l[k] == -l[i] and c not in res and j != k:
                        res.append(c)
                    elif l[j] + l[k] > -l[i]:
                        j -= 1
                    else:
                        k += 1
                i += 1
      
        return res