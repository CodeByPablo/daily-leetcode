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

        # # Step by step solution
        # # check for values in row
        # for row in range(9):
        #     seen = set()
        #     for column in range(9):
        #         item = board[row][column]
        #         if item in seen:
        #             return False
        #         elif item != ".":
        #             seen.add(item)
        # # check for values in column
        # for row in range(9):
        #     seen = set()
        #     for column in range(9):
        #         item = board[column][row]
        #         if item in seen:
        #             return False
        #         elif item != ".":
        #             seen.add(item)
        # # check for values in boxes
        # starts = [(0, 0), (0, 3), (0, 6),
        #           (3, 0), (3, 3), (3, 6),
        #           (6, 0), (3, 3), (6, 6)]
        
        # for i, j in starts:
        #     seen = set()
        #     for row in range(i, i+3):
        #         for col in range(j, j+3):
        #             item = board[row][col]
        #             if item in seen:
        #                 return False
        #             elif item != ".":
        #                 seen.add(item)
        # return True



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


