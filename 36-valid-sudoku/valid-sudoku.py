class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
               
        for i in range(9):
            checkrow = [0] *9
            checkcol = [0] *9
            for j in range(9):
                if board[i][j].isdigit():
                    checkrow[int(board[i][j])-1] += 1
                    if checkrow[int(board[i][j])-1] > 1:
                        return False
                if board[j][i].isdigit():
                    checkcol[int(board[j][i])-1] += 1
                    if checkcol[int(board[j][i])-1] > 1:
                        return False
        for i in range(0,9,3):
            for j in range(0,9,3):
                boxes = [0]*9
                for k in range(3):
                    for l in range(3):
                        if board[k+i][l+j].isdigit():
                            boxes[int(board[k+i][j+l])-1] += 1
                            if boxes[int(board[k+i][j+l])-1] > 1:
                                return False
        return True