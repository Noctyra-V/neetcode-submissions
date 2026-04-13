class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_dict = {}
        for i,v in enumerate(nums):
            my_dict.setdefault(v,[]).append(i)
        print(my_dict)
        for n in nums:
            res = []
            if target - n in my_dict and my_dict[n] != my_dict[target - n] and len(my_dict[n]) == 1 and len(my_dict[target - n]) == 1:
                return [my_dict[n][0],my_dict[target - n][0]]
            elif target - n in my_dict and len(my_dict[n]) == 2:
                return [my_dict[n][0],my_dict[n][1]]
            
        return []

