class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_dict = {}
        for i,n in enumerate(nums):
            if target - n not in my_dict:
                my_dict[n] = i
            else:
                return [my_dict[target - n],i]
        return []
# complexity => time:o(n) and space:o(n)