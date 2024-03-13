class Solution:
    def matrixDiagonally(self,mat):
        n = len(mat)
        i, j = 0, 0
        is_up = True
    
        res = []
    
        for _ in range(n * n):
            res.append(mat[i][j])
    
            if is_up:
                if j == n - 1:
                    i += 1
                    is_up = False
                elif i == 0:
                    j += 1
                    is_up = False
                else:
                    i -= 1
                    j += 1
            else:
                if i == n - 1:
                    j += 1
                    is_up = True
                elif j == 0:
                    i += 1
                    is_up = True
                else:
                    i += 1
                    j -= 1
    
        return res