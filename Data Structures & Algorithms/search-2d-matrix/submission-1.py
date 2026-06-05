class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows=len(matrix)
        cols=len(matrix[0])
        for i in range(rows):
            if target<matrix[i][cols-1]:
                l=0
                r=cols-1
                while l<=r:
                    mid= l + (r-l)//2
                    if matrix[i][mid]==target:
                        return True
                    elif matrix[i][mid]>target:
                        r=mid-1
                    else:
                        l=mid+1
            elif target==matrix[i][cols-1] :
                return True
        if target not in matrix:
            return False
            
                
