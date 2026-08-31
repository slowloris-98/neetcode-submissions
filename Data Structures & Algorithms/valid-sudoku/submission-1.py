class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # row
        for r in range(9):
            curr=set()
            for c in range(9):
                if board[r][c] in curr:
                    return False
                if board[r][c]!=".":
                    curr.add(board[r][c])
        
        # col
        for c in range(9):
            curr=set()
            for r in range(9):
                if board[r][c] in curr:
                    return False
                if board[r][c]!=".":
                    curr.add(board[r][c])

        # square
        for i in range(0,9,3):
            for j in range(0,9,3):
                curr=set()
                for r in range(i,i+3):
                    for c in range(j,j+3):
                        if board[r][c] in curr:
                            return False
                        if board[r][c]!=".":
                            curr.add(board[r][c])

        return True



        
            