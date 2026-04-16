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
        k = 0
        i = 0
        seenin_box = [[] for _ in range(0,9)]
        seen_col = [[] for _ in range(0,9)]
        for i,v in enumerate(board):
            seen = []
            for j,v in enumerate(board[i]):
                box_indx = self.in_box(i,j)
                if v.isdigit() and v in seen or v.isdigit() and v in seen_col[j] or v.isdigit() and v in seenin_box[box_indx]:
                    return False
                elif v.isdigit():
                    seenin_box[box_indx].append(v)
                    seen_col[j].append(v)
                    seen.append(v)
                    print("seen",seen)

        return True


# my solution with help with inbox: complexity => time: o(n^2) and space: (n*m) which n is number of rows and m number of columns (removed the columns loop)
