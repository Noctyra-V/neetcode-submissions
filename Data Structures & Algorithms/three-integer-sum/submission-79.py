class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        my_dict = {}
        i = 0 
        nums.sort()
        k = i + 1
        j = len(nums) - 1
        output = []
        while i < len(nums) - 1:
            if i > 0 and nums[i] ==  nums[i - 1]:
                i+=1
                continue
            k = i + 1
            j = len(nums) - 1

            while k < j:
                if -nums[i] == nums[j] + nums[k]:
                    output.append([nums[i],nums[j],nums[k]])
                    k += 1
                    while k < j and nums[k] == nums[k-1]:
                        k += 1
                if nums[i] + nums[j] < -nums[k]:
                    k += 1
                if nums[i] + nums[j] > -nums[k]:
                    j -= 1

            i+=1
        return output