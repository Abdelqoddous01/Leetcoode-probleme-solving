class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        isvalidsudoko=True

        for l in board:
            forvalidation=[]
            for i in l:
                if i.isnumeric():
                    forvalidation.append(i)
            if(len(set(forvalidation))!=len(forvalidation)):
                isvalidsudoko=False
                break        
            
        if isvalidsudoko:    
            for i in range(0,9):
                forvalidation=[]
                for l in board:
                    if l[i].isnumeric():
                        forvalidation.append(l[i])
                if(len(set(forvalidation))!=len(forvalidation)):
                    isvalidsudoko=False
                    break   
            
        squares=[]
        l1=[]
        l2=[]
        l3=[]
        l4=[]
        l5=[]
        l6=[]
        l7=[]
        l8=[]
        l9=[]
        if isvalidsudoko:      
            for i in range(0,9):
                for j in range(0,3):
                    if board[i][j].isnumeric():
                        if i>=0 and i<3:
                            l1.append(board[i][j])
                        elif i>=3 and i<6:
                            l2.append(board[i][j])
                        else:
                            l3.append(board[i][j])
                
                for j in range(3,6):
                    if board[i][j].isnumeric():
                        if i>=0 and i<3:
                            l4.append(board[i][j])
                        elif i>=3 and i<6:
                            l5.append(board[i][j])
                        else:
                            l6.append(board[i][j])
                
                for j in range(6,9):
                    if board[i][j].isnumeric():
                        if i>=0 and i<3:
                            l7.append(board[i][j])
                        elif i>=3 and i<6:
                            l8.append(board[i][j])
                        else:
                            l9.append(board[i][j])

            squares.append(l1)
            squares.append(l2)
            squares.append(l3)
            squares.append(l4)
            squares.append(l5)
            squares.append(l6)
            squares.append(l7)
            squares.append(l8)
            squares.append(l9)

        for l in squares:
            print(l)

        for l in squares:
            if len(set(l))!=len(l):
                isvalidsudoko=False
                break

        return isvalidsudoko
