class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        for r in range(9):

            checked = set()
            for c in range(9):

                if board[r][c] == ".":
                    continue
                elif board[r][c] in checked:
                    return False
                else:
                    checked.add(board[r][c])

        for c in range(9):
            
            checked = set()
            for r in range(9):
                
                if board[r][c] == ".":
                    continue
                elif board[r][c] in checked:
                    return False
                else:
                    checked.add(board[r][c])
        
        for square in range(9):

            checked = set()
            for r in range(3):
                for c in range(3):
                    
                    row = (square // 3) * 3 + r
                    col = (square % 3) * 3 + c

                    if board[row][col] == ".":
                        continue

                    elif board[row][col] in checked:
                        return False
                    else:
                        checked.add(board[row][col])

        return True



        