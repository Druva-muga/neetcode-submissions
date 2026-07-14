class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = [""]*9
        col = [""]*9
        box = [[""]*3 for _ in range(3)]

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == ".":
                    continue
                if board[i][j] not in row[i]:
                    row[i]+=board[i][j]
                else:
                    return False
                if board[i][j] not in col[j]:
                    col[j]+=board[i][j]
                else:
                    return False
                if board[i][j] not in box[i//3][j//3]:
                    box[i//3][j//3]+=board[i][j]
                else:
                    return False
        return True
                

        