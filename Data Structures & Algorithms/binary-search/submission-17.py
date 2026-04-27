class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            middle = (left + right) // 2
            if middle >= len(nums):
                break
            if  nums[middle] == target:
                return middle
            elif nums[middle] > target:
                right = middle-1
            elif nums[middle] < target:
                left = middle+1
        return -1

# solution avoiding slicing inside loop which added complexity to time
# now the complexity is:
# time:o(log n) and space:o(1)
        