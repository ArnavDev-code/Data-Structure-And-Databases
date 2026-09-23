class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        # Create arrays of sets to track numbers seen so far
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        
        for r in range(9):
            for c in range(9):
                val = board[r][c]
                
                # Skip empty spaces
                if val == '.':
                    continue
                
                # Map the 2D row/col index into a 0-8 box index
                box_idx = (r // 3) * 3 + (c // 3)
                
                # Check for duplicates in row, column, or 3x3 box
                if val in rows[r] or val in cols[c] or val in boxes[box_idx]:
                    return False
                
                # Document the value in our sets
                rows[r].add(val)
                cols[c].add(val)
                boxes[box_idx].add(val)
                
        return True
