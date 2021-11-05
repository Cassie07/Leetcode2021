class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        # row
        # column
        # sub-box
        row = {i:[] for i in range(len(board))}
        column = {j:[] for j in range(len(board))}
        sub_box = {(i,j):[] for i in range(3) for j in range(3)}
        
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == '.': continue
                
                # row
                if board[i][j] not in row[i]: row[i].append(board[i][j])
                else:
                    return False
                
                # column
                if board[i][j] not in column[j]: column[j].append(board[i][j])
                else:
                    return False
                
                # sub-box
                if board[i][j] not in sub_box[(i//3,j//3)]: sub_box[(i//3,j//3)].append(board[i][j])
                else:
                    return False
        return True
