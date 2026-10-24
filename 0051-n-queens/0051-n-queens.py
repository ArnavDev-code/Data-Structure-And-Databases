class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        # Track occupied vertical and diagonal paths
        cols = set()
        pos_diag = set()  # (row + col)
        neg_diag = set()  # (row - col)
        
        res = []
        # Initialize an empty n x n board
        board = [["."] * n for _ in range(n)]
        
        def backtrack(row: int):
            # Base case: All queens are successfully placed
            if row == n:
                # Convert the board grid into the required list of strings
                copy = ["".join(r) for r in board]
                res.append(copy)
                return
            
            # Try placing a queen in each column of the current row
            for col in range(n):
                # Check if the current position is under attack
                if col in cols or (row + col) in pos_diag or (row - col) in neg_diag:
                    continue
                
                # Place the queen and update state
                board[row][col] = "Q"
                cols.add(col)
                pos_diag.add(row + col)
                neg_diag.add(row - col)
                
                # Move to the next row
                backtrack(row + 1)
                
                # Backtrack: Remove the queen and restore state
                board[row][col] = "."
                cols.remove(col)
                pos_diag.remove(row + col)
                neg_diag.remove(row - col)
                
        backtrack(0)
        return res
