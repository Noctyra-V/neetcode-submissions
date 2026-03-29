class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        my_dict = {}
        for num in nums:    
            if num in my_dict:
                my_dict[num] += 1
            else:
                my_dict[num] = 1
        max_items = 0
        biggest = []
        while max_items < k:
            biggest_key = 0
            most = -1
            for key,v in my_dict.items():
                if my_dict[key] > most and key not in biggest:
                    most = my_dict[key]
                    biggest_key = key
            biggest.append(biggest_key)
            max_items += 1
        return biggest