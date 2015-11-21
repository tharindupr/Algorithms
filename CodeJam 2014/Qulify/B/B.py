def whichisbetter(C,F,f,X):
    if((C/f+X/(f+F))<X/f):
        return(1)
    else:
        return(0)

file=open("B-large.in","r")
cases=int(file.readline()[:-1])
for i in range(cases):
    numberstring=file.readline()[:-1].split()
    numbers=[]
    for x in numberstring:
        numbers.append(float(x))
        
    C=numbers[0]
    F=numbers[1]
    X=numbers[2]

    time=0
    f=2

    if(X<C):
        print("Case #"+str(i+1)+": "+str(X/2))

    else:
        count=0
        while(count<X):
            if(whichisbetter(C,F,f,X)):
                time=time+C/f
                f=f+F

            else:
                time=time+(X/f)
                break
        print("Case #"+str(i+1)+": "+str(time))
            
        
        
        




 
