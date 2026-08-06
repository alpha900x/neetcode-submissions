class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

       #check rows
        for i in board:
            hp={}
            for j in i:
                if j=='.':
                    continue
                if j not in hp:
                    hp[j]=1
                else:
                    return False
                    
        #check columns
        for i in range(9):
            hp={}
            for j in range(9):
                if board[j][i]=='.':
                    continue
                if board[j][i] not in hp:
                    hp[board[j][i]]=1
                else:
                    return False

        #check individual boxes
        for r in range(0,9,3):
            for c in range(0,9,3):
                hp={}
                for i in range(3):
                    for j in range(3):
                        if board[i+r][j+c]=='.':
                            continue
                        if board[i+r][j+c] not in hp:
                            hp[board[i+r][j+c]]=1
                        else:
                            return False

        return True
    

                    