def moves(x,y,p):
     board=[]
     for k in range(0,8):
          board.append([])
          for l in range(0,8):
               board[l].append(0)
     
     if(p=="R" or p=="r"):
          for j in range(0,8):
               board[x][j]=1

          for i in range(0,8):
               board[i][y]=1
               
          
          
     return(board)  
