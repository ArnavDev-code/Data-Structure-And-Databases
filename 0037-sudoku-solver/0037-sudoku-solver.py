class Solution:
    def solveSudoku(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # Tracks used digits for rows, columns, and 3x3 boxes
        rows = [0] * 9
        cols = [0] * 9
        boxes = [0] * 9
        
        # Helper to compute the box index from row and col
        get_box = lambda r, c: (r // 3) * 3 + (c // 3)
        
        # Populate the initial state with pre-filled numbers
        empty_cells = []
        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    empty_cells.append((r, c))
                else:
                    val = int(board[r][c])
                    mask = 1 << val
                    rows[r] |= mask
                    cols[c] |= mask
                    boxes[get_box(r, c)] |= mask
        
        def backtrack(cell_idx: int) -> bool:
            # Base case: successfully filled all empty cells
            if cell_idx == len(empty_cells):
                return True
                
            r, c = empty_cells[cell_idx]
            b = get_box(r, c)
            
            # Combine masks to see what numbers are already taken in this row, col, and box
            taken = rows[r] | cols[c] | boxes[b]
            
            # Try digits 1 through 9
            for num in range(1, 10):
                mask = 1 << num
                # If the bit is not set, this number is available
                if not (taken & mask):
                    # Place the number
                    board[r][c] = str(num)
                    rows[r] |= mask
                    cols[c] |= mask
                    boxes[b] |= mask
                    
                    # Recursively move to the next empty cell
                    if backtrack(cell_idx + 1):
                        return True
                    
                    # Backtrack (Undo placement)
                    board[r][c] = '.'
                    rows[r] &= ~mask
                    cols[c] &= ~mask
                    boxes[b] &= ~mask
                    
            return False

        backtrack(0)
