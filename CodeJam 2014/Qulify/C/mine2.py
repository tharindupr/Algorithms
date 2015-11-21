import math
file = open("C-small-practice.in","r")
outfile=open("outl.txt","w")
t_case=file.readline()

def last(board,R,C,M):
    #print("last")
    #print(empty)
    empty=(R*C)-M
    sqr=int(math.sqrt(empty)//1)
    for x in range(R,1,-1):
        remain=empty-sqr**2
        #print(R,sqr,remain)
        #print(empty)
        if remain==1:
            return
        if empty>9 and (R>=sqr and C>=sqr):
            k=0
            l=0
            #print(C,sqr)
            for k in range(0,sqr):
                for l in range(0,sqr):
                    board[k][l]="."
            if R>sqr and C>remain:
                print("as")
                for x in range(0,remain):
                    board[x][l+1]="."
                for q in range(0,len(board)):
                    for r in range(0,len(board[0])):
                        if board[q][r]==None:
                            board[q][r]="*"
                board[0][0]="c"
                return board
            elif C>sqr and R>remain:

                for x in range(0,remain):
                    board[k+1][x]="."
                for q in range(0,len(board)):
                    for r in range(0,len(board[0])):
                        if board[q][r]==None:
                            board[q][r]="*"
                board[0][0]="c"
                return board
            elif R>sqr+1 and C<=remain:

                for x in range(0,sqr):
                    board[x][l+1]="."
                for x in range(0,remain-sqr):
                    board[x][l+2]="."
                for q in range(0,len(board)):
                    for r in range(0,len(board[0])):
                        if board[q][r]==None:
                            board[q][r]="*"
                board[0][0]="c"
                return board
            elif C>sqr+1 and R<=remain:

                for x in range(0,sqr):
                    board[k+1][x]="."
                for x in range(0,remain-sqr):
                    board[k+2][x]="."
                for q in range(0,len(board)):
                    for r in range(0,len(board[0])):
                        if board[q][r]==None:
                            board[q][r]="*"
                board[0][0]="c"
                return board
def settle(board,R,C,M):
    #print(size)
    #print(empty)
    empty=(R*C)-M
    if empty==1:
        board[0][0]="c"
        for q in range(0,len(board)):
            for r in range(0,len(board[0])):
                if board[q][r]==None:
                    board[q][r]="*"
        return board
    elif R==1 :
        for x in range(0,empty):
            board[x][0]="."
        for q in range(0,len(board)):
            for r in range(0,len(board[0])):
                if board[q][r]==None:
                    board[q][r]="*"
        board[0][0]="c"
        return board
    elif C==1 :
        for x in range(0,empty):
            board[0][x]="."
        for q in range(0,len(board)):
            for r in range(0,len(board[0])):
                if board[q][r]==None:
                    board[q][r]="*"
        board[0][0]="c"
        return board
    elif (R==M or C==M)and(R>2 and C>2):
        if R==M:
            for x in range(0,M):
                board[0][x]="*"
        elif C==M:
            for x in range(0,M):
                board[x][0]="*"
        for q in range(0,len(board)):
            for r in range(0,len(board[0])):
                if board[q][r]==None:
                    board[q][r]="."
        board[len(board)-1][len(board[0])-1]="c"
        return board
    elif empty==4:
        board[0][0]="."
        board[0][1]="."
        board[1][0]="."
        board[1][1]="."
        for q in range(0,len(board)):
            for r in range(0,len(board[0])):
                if board[q][r]==None:
                    board[q][r]="*"
        board[0][0]="c"
        return board
    else:
        for x in range(R,1,-1):
            remain=empty%x
            if (remain==0 and empty/x>2) and empty/x<= C:
                for k in range(0,int(empty/x)):
                    for l in range(0,x):
                        board[k][l]="."
                for q in range(0,len(board)):
                    for r in range(0,len(board[0])):
                        if board[q][r]==None:
                            board[q][r]="*"
                board[0][0]="c"
                return board
            elif (remain==0 and empty/x==2) and (R==2 or C==2):
                for k in range(0,int(empty/x)):
                    for l in range(0,x):
                        board[k][l]="."
                for q in range(0,len(board)):
                    for r in range(0,len(board[0])):
                        if board[q][r]==None:
                            board[q][r]="*"
                board[0][0]="c"
                return board
        for v in range(C,1,-1):
            k=0
            l=0
            remain=empty%v
            if (remain==0 and empty/v>2) and empty/v<= R:
                for k in range(0,v):
                    for l in range(0,int(empty/v)):
                        #print(v)
                        board[k][l]="."
                for q in range(0,len(board)):
                    for r in range(0,len(board[0])):
                        if board[q][r]==None:
                            board[q][r]="*"
                board[0][0]="c"
                return board
            elif (remain==0 and empty/v==2) and (R==2 or C==2):
                for k in range(0,v):
                    for l in range(0,int(empty/v)):
                        board[k][l]="."
                for q in range(0,len(board)):
                    for r in range(0,len(board[0])):
                        if board[q][r]==None:
                            board[q][r]="*"
                board[0][0]="c"
                return board

        fin=last(board,R,C,M)
        if fin!=None:
            return fin

        if M<empty/2:
            count=M
            if R>C:
                x=0
                y=0
                for x in range(0,len(board)):
                    for y in range(0,len(board[0])):
                        #print(y)
                        if count>0:
                            board[x][y]="*"
                            count-=1
                        else:
                            y-=1
                            break
                    if count<1:
                        break
                for q in range(0,len(board)):
                    for r in range(0,len(board[0])):
                        if board[q][r]==None:
                            board[q][r]="."

                #print(board)
                try:
                    #print(x,y)
                    if board[x+2][y+2]==".":

                        board[len(board)-1][len(board[0])-1]="c"
                        return board
                    else:
                        return "Impossible"
                except:
                    print("sd")
                    return "Impossible"
            else:
                #print("el")
                x=0
                y=0
                for x in range(0,len(board[0])):
                    for y in range(0,len(board)):
                        if count>0:
                            board[y][x]="*"
                            count-=1
                        else:
                            y-=1
                            break
                    if count<1:
                        break
                for q in range(0,len(board)):
                    for r in range(0,len(board[0])):
                        if board[q][r]==None:
                            board[q][r]="."
                try:
                    if board[y+2][x+2]==".":
                        board[len(board)-1][len(board[0])-1]="c"
                        return board
                    else:
                        return "Impossible"
                except:
                    return "Impossible"


        return "Impossible"
for ko in range(0,int(t_case)):
    txt=file.readline().split()
    R=int(txt[0])
    C=int(txt[1])
    M=int(txt[2])

    board=[None]*C
    for k in range(0,len(board)):
        temp=[None]*R
        board[k]=temp


    listo=settle(board,R,C,M)
    out="Case #"+str(ko+1)+": \n"
    if listo=="Impossible":
        out+=listo
    else:
        for q in range(0,len(board[0])):
            for r in range(0,len(board)):
                out+=board[r][q]
            out+="\n"
        out=out[:-1]
    outfile.write(out+"\n")
    print(out)
