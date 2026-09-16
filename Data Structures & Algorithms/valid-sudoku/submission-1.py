class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # row-wise
        for row in board:
            seen = set()
            for char in row:
                if char != '.':
                    if char in seen:
                        return False
                    seen.add(char)

        # column-wise
        num_cols = len(board)
        num_rows = len(board[0])
        for c in range(num_rows):
            seen = set()
            for r in range(num_cols):
                char = board[r][c]
                if char != '.':
                    if char in seen:
                        return False
                    seen.add(char)
        
        # square-wise
        for square in range(9):
            seen = set()
            for i in range(3):
                for j in range(3):
                    row = (square//3) * 3 + i
                    col = (square%3) * 3 + j
                    if board[row][col] != ".":
                        if board[row][col] in seen:
                            return False
                        seen.add(board[row][col])
        
        return True