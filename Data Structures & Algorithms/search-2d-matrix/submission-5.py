class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        y=len(matrix[0])-1
        r=0
        if target> matrix[len(matrix)-1][y]:
            return False
        for i in range(len(matrix)):
            if target<=matrix[i][y]:
                r=i
                break
        l=0
        h=y
        while l<=h:
            mid=int((l+h)/2)
            if target==matrix[r][mid]:
                return True
            if target>matrix[r][mid]:
                l=mid+1
            if target<matrix[r][mid]:
                h=mid-1
        return False

