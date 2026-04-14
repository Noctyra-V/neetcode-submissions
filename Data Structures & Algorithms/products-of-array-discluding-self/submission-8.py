class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        i = 0
        result = [1] * len(nums)
        left = 0
        res = 1
        right = len(nums) - 1
        while i < len(nums):
           
            if left >= right :
                if right != i and len(nums) % 2 == 0:
                    res *= nums[right]
                result[i] = res
                res = 1
                left = 0
                right = len(nums) - 1
                i+=1
                continue

            if left == i:
                left += 1
                continue
            if right == i:
                right -= 1
                continue

            res *= nums[left] * nums[right]
            left += 1
            right -= 1
        return result

# my other attempt still o(n^2)
