class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        i = 0
        res = 1
        result = []
        j = 0
        while i < len(nums):
            if j == i:
                j += 1
                continue
            if j == len(nums):
                result.append(res)
                res = 1
                i += 1
                j = 0
            else:
                res *= nums[j]
                j += 1
        return result

# my first attempt