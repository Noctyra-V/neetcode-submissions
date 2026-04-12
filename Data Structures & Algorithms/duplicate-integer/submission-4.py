class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        my_dict = {}
        for i in range(0,len(nums)):
            if my_dict.get(nums[i]) == 1:
                return True
            else:
                my_dict[nums[i]] = 1
        return False
