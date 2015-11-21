import math


        


def nsquare(n):
    a=math.sqrt(n)//1
    return(a**2)

def checker(x,y,array):

    return(array[x][y+1]+array[x+1][y+1]+array[x+1][y]+array[x-1][y+1]+array[x+1][y-1]+array[x-1][y]+array[x-1][y-1]+array[x][y-1])

def clear(x,y,array):
    for i in range(0,x+1):
        for j in range(0,y+1):
            array[i][j]=0
def nclear(x,y,array):
    array[x][y+1]=0
    array[x+1][y+1]=0
    array[x+1][y]=0
    array[x-1][y+1]=0
    array[x+1][y-1]=0
    array[x-1][y]=0
    array[x-1][y-1]=0
    array[x][y-1]=0
def printfield_nob(array):
    array1=array
    for i in range(len(array1)):
        for j in range(len(array[i])):
            
            if(i==1 and j==1):
                    array[i][j]="c"
            else:
                    array[i][j]="."
            
      
    for i in range(1,len(array1)-1):
        pattern="" 
        for j in range(1,len(array1[i])-1):
            pattern+=str(array1[i][j])
        print(pattern)
        
def printfield(array):
    array1=array
    for i in range(len(array1)):
        for j in range(len(array[i])):
            if(array[i][j]==0):
                if(i==1 and j==1):
                    array[i][j]="c"
                else:
                    array[i][j]="."
            else:
                array[i][j]="*"
      
    for i in range(1,len(array1)-1):
        pattern="" 
        for j in range(1,len(array1[i])-1):
            pattern+=str(array1[i][j])
        print(pattern)

def printer(a,b,f):
    if(f==0):
        
        for x in range(a-1):
            if(x==0):
               print('c'+'.'*(b-1))
            else:
               print('.'*b)
        print('*'*b)
    else:
        for x in range(a):
            if(x==0):
               print('c'+'.'*(b-2)+'*')
            else:
               print('.'*(b-1)+'*')
            
            
file=open("C-small-attempt0.in","r")
cases=int(file.readline()[:-1])

for k in range(cases):
    
    line=file.readline()[:-1].split(" ")
    r=int(line[0])
    c=int(line[1])
    bombs=int(line[2])
    total=c*r
    target=total-bombs
    array=[]
    for x in range(r+2):
        array.append([])

    for y in range(0,len(array)):
        for z in range(c+2):
            if(y==0):
             array[y].append(0)

            elif(y+1==len(array)):
             array[y].append(0)
            else:
                if(z==0):
                    array[y].append(0)
                elif(z+1==c+2):
                    array[y].append(0)
                else:
                    array[y].append(1)

        
    squares=[1,4,9,16,25,36,49,64,81,100,121,144,169,196,225,256,289,324,361,400,441,484]
    flag=0
    flag2=0
    if int(nsquare(target)) in squares:
        if(int(nsquare(target))==target):
            no=int(nsquare(target))
            x=int(math.sqrt(no))
            y=int(math.sqrt(no))

            if(c>=int(math.sqrt(target)) and r>=int(math.sqrt(target))):
                flag=1
                clear(x,y,array)

            
            
            else:
                if(bombs<c):
                    flag2=1
                    flag=0
                else:
                    flag=0
            
        elif(bombs!=0):
            #print(line)
            #print(c)
            #print(r)
            no=int(nsquare(target))
            x=int(math.sqrt(no))
            y=int(math.sqrt(no))
            clear(x,y,array)

            for h in range(1,x+1):
                if(no+checker(h,y,array)==target):
                    flag=1
                    nclear(h,y,array)
                    break
            if(flag==0):        
                for h in range(1,y+1):
                    if(no+checker(x,h,array)==target):
                        flag=1
                        nclear(x,h,array)
                        break

    if(target<=1):
        flag=0
    if(bombs==0):
        flag=1

    
    if(target==1):
        print("Case #"+str(k+1)+":")
        print('c'+'*'*(c-1))
        for o in range(r-1):
            print('*'*c)
        
    elif(flag==1 and bombs!=0):
        print("Case #"+str(k+1)+":")
        printfield(array)
    elif(flag==1 and bombs==0):
        print("Case #"+str(k+1)+":")
        printfield_nob(array)
    elif(flag2==1):
        print("Case #"+str(k+1)+":")
        for b in range(0,r):
            if(b==0):
                print("*"*bombs+'.'*(c-bombs))
            if(b!=r-1):
                print('.'*c)
            else:
                print('.'*(c-1)+'c')
    else:
        
                    
        if((bombs==c and (r-1)>=2)  or (bombs==r and (c-1)>=2)):
            #print(bombs)
            #print(r)
            #print(c)
            print("Case #"+str(k+1)+":")
            if((bombs==c) and (c-1)>=2):
               printer(r,c,0)
            elif(bombs==r and (r-1)>=2):
               printer(r,c,1)
        else:          
            print("Case #"+str(k+1)+":")
            print("Impossible") 
            
   # print(str(bombs))   
    

        
    
