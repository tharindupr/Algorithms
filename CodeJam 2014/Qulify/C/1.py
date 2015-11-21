def checker(x,y,a):
    return(a[x][y]+a[x-1][y-1]+a[x-1][y]+a[x-1][y+1]+a[x][y-1]+a[x][y+1]+a[x+1][y-1]+a[x+1][y]+a[x+1][y+1])
def clear(x,y,a):
    a[x][y]=0
    a[x-1][y-1]=0
    a[x-1][y]=0
    a[x-1][y+1]=0
    a[x][y-1]=0
    a[x][y+1]=0
    a[x+1][y-1]=0
    a[x+1][y]=0
    a[x+1][y+1]=0
file=open("C-small-attempt0.in","r")
count=int(file.readline()[:-1])
for p in range (count):
    print("Case #"+str(p+1)+":")
    data=file.readline()[:-1].split(" ")
    r=int(data[0])
    c=int(data[1])
    bombs=int(data[2])
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
    total=r*c-bombs
    ad=0
    if(total==1):
        for k in range (1,r+1):
                for l in range (1,c+1):
                    if(k==1)and(l==1):
                        st="c"
                    elif(array[k][l]==1):
                        st=st+"*"
                if(k!=r):
                    st=st+"\n"
        print(str(st))
    elif(checker(1,1,array)>total):
        print("Impossible")
    elif(checker(1,1,array)<total)or(checker(1,1,array)==total):
        x=1
        while(ad<total):
            y=1
            while(ad<total):
                count=0
                ad+=checker(x,y,array)
                if((array[x+1][y+1]==0)and(array[x][y+1]==0)):
                    count+=1
                clear(x,y,array)
                y+=1
                if(count==1):
                    break
            x+=1
            if((x==r)and(y==c)):
                break
        if(ad>total):
            print("Impossible")
        if(ad==total):
            for k in range (1,r+1):
                for l in range (1,c+1):
                    if(k==1)and(l==1):
                        st="c"
                    elif(array[k][l]==0):
                        st=st+"."
                    elif(array[k][l]==1):
                        st=st+"*"
                if(k!=r):
                    st=st+"\n"
    if(ad==total):
        print(str(st))

