class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        
        row,column = len(mat), len(mat[0])
        
        for i in range (row):
            for j in range(column):
                if mat[i][j] == 0:
                    continue
                else:
                    if mat[i][j] > 0:
                        mat[i][j] = min(mat[i-1][j] if i>0 else float('inf'), mat[i][j-1] if j>0 else float('inf')) + 1
        for i in range(row -1,-1,-1):
            for j in range(column-1, -1, -1):
                if mat[i][j] > 0:
                    mat[i][j] = min(mat[i][j], mat[i+1][j] + 1 if i < row -1 else float('inf'), mat[i][j+1] + 1 if j < column-1 else float('inf'))            
        return mat
