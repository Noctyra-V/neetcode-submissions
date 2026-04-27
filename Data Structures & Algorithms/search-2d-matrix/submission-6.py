class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for l in matrix:
            left = 0
            right = len(l) - 1
            while True:
                middle = (left + right) // 2
                if  l[middle] == target:
                    return True
                if l[left:right] == []:
                    break
                elif l[middle] > target:
                    right = middle-1
                elif l[middle] < target:
                    left = middle+1
        return False
        

