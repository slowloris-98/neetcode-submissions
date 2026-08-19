class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res=[]
        m,n = len(matrix), len(matrix[0])
        left,right,top,bottom = 0, n-1, 0, m-1
        
        while left<=right and top<=bottom:
            
            # left to right
            i=left
            while i<=right:
                res.append(matrix[top][i])
                i+=1
            top+=1
            
            # top to bottom
            i=top
            while i<=bottom:
                res.append(matrix[i][right])
                i+=1
            right-=1

            if not (left<=right and top<=bottom):
                break

            # right to left
            i=right
            while i>=left:
                res.append(matrix[bottom][i])
                i-=1
            bottom-=1

            # bottom to top
            i=bottom
            while i>=top:
                res.append(matrix[i][left])
                i-=1
            left+=1

        return res

