class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        N = 9
        row_hashes = [set() for _ in range(N)]
        column_hashes = [set() for _ in range(N)]
        box_hashes = [set() for _ in range(N)]
        
        for r in range(N):
            for c in range(N):
                val = board[r][c]
                if val != '.':
                    if (val in row_hashes[r]) or (val in column_hashes[c]) or (val in box_hashes[(r//3)*3 + (c//3)]):
                        return False
                    row_hashes[r].add(val)
                    column_hashes[c].add(val)
                    box_hashes[(r//3)*3 + (c//3)].add(val)
                    
                else:
                    continue
        return True