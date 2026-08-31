class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        cols = defaultdict(set)
        rows = defaultdict(set)
        squares = defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] in rows[r] or board[r][c] in cols[c] or board[r][c] in squares[(r//3,c//3)]:
                    return False
                if board[r][c] != ".":
                    rows[r].add(board[r][c])
                    cols[c].add(board[r][c])
                    squares[(r//3,c//3)].add(board[r][c])
        return True



        # # row
        # for r in range(9):
        #     curr=set()
        #     for c in range(9):
        #         if board[r][c] in curr:
        #             return False
        #         if board[r][c]!=".":
        #             curr.add(board[r][c])
        
        # # col
        # for c in range(9):
        #     curr=set()
        #     for r in range(9):
        #         if board[r][c] in curr:
        #             return False
        #         if board[r][c]!=".":
        #             curr.add(board[r][c])

        # # square
        # for i in range(0,9,3):
        #     for j in range(0,9,3):
        #         curr=set()
        #         for r in range(i,i+3):
        #             for c in range(j,j+3):
        #                 if board[r][c] in curr:
        #                     return False
        #                 if board[r][c]!=".":
        #                     curr.add(board[r][c])

        # return True



        
            