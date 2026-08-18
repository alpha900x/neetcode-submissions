class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ha=len(matrix)-1
        la=0
        while ha>=la:
            ma=(la+ha)//2
            if target > matrix[ma][-1]:
                la = ma+1
            elif target < matrix[ma][0]:
                ha = ma-1
            else:
                h=len(matrix[ma])-1
                l=0
                while h>=l :
                    m=(l+h)//2
                    if target > matrix[ma][m]:
                        l=m+1 
                    elif target < matrix[ma][m]:
                        h=m-1
                    else:
                        return True
                return False
        return False