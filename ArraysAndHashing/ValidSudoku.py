from collections import defaultdict
from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        columns = defaultdict(set)
        boxes = defaultdict(set)

        for row in range(9):
            for column in range(9):
                item = board[row][column]
                # check for given condition, if condition TRUE return FALSE
                if (item in rows[row] or 
                    item in columns[column] or
                    item in boxes[(row // 3, column // 3)]):
                    return False
                # if not FALSE && not "." add to set
                elif item != ".":
                    rows[row].add(item)
                    columns[column].add(item)
                    boxes[(row // 3, column // 3)].add(item)
                #continue
        return True

board = [
    ["5","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
]

solution = Solution()
print(solution.isValidSudoku(board))


