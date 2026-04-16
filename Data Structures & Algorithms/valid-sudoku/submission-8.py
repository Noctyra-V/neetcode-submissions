class Solution:
    def in_box(self, i,j):
        if 0 <= i <= 2 and 0 <= j <= 2:
            return 0
        if 0 <= i <= 2 and 3 <= j <= 5:
            return 1
        if 0 <= i <= 2 and 6 <= j <= 8:
            return 2  
        if 3 <= i <= 5 and 0 <= j <= 2:
            return 3  
        if 3 <= i <= 5 and 3 <= j <= 5:
            return 4  
        if 3 <= i <= 5 and 6 <= j <= 8:
            return 5  
        if 6 <= i <= 8 and 0 <= j <= 2:
            return 6  
        if 6 <= i <= 8 and 3 <= j <= 5:
            return 7  
        if 6 <= i <= 8 and 6 <= j <= 8:
            return 8
        
    def isValidSudoku(self, board: List[List[str]]) -> bool:
      
        seen_box = [{},{},{},{},{},{},{},{},{}]
        seen_col = [{},{},{},{},{},{},{},{},{}]

        for i,row in enumerate(board):
            seen_row = {}
            for j,col in enumerate(row):
                if col.isdigit():
                    bx_index = self.in_box(i,j)
                    if col in seen_row or col in seen_col[j] or col in seen_box[bx_index]:
                        return False
                    else:
                        seen_box[bx_index][col] = (i,j) 
                        seen_col[j][col] = (i,j)
                        seen_row[col] = (i,j)
        return True

# my solution with help with inbox: complexity => time: o(n^2) and space: (n*m) which n is number of rows and m number of columns (removed the columns loop)
