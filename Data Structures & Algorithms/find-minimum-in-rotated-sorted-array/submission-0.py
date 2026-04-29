class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        m = float("inf")
        while left <=  right:
            middle = (left + right) // 2

            if nums[middle] < m:
                m = nums[middle]
            if nums[-1] <= nums[middle]:
                left = middle + 1
            else:
                right = middle - 1
        return m