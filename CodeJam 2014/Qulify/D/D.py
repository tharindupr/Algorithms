file=open("D-large.in",'r')

nm = int(file.readline().strip('\n'))
tharindu=open('new.out','w')


k=1
while k <= nm:
    a=[]
    b=[]
    count=file.readline()
    aa=file.readline().strip().split()
    bb=file.readline().strip().split()
    for i in aa:
        a.append(float(i))
    for i in bb:
        b.append(float(i))
    


    n=[]
    s=[]

    a.sort()
    b.sort()

    
              
    i=0

    d=0
    
    while len(a)>0:
        if a[0] < b[0]:
            t=a.pop(0)
            n.append(t)
            t=b.pop()
            s.append(t)
        else:
            j=len(b)-1
            
            while a[0]<b[j]:
                
                    
                j=j-1
            t=a.pop(0)
            n.append(t)
            t=b.pop(j)
            s.append(t)
            d=d+1

    n.sort()
    s.sort()
    w=0
    while len(n)>0:
        j=0
        try:
            while n[0]> s[j]:
                j=j+1
                
            s.pop(j)
            n.pop(0)
            
        except:
            w=len(n)
            break
    tharindu.write("Case #"+str(k)+": "+str(d)+" "+str(w)+'\n' )
    k=k+1
            
tharindu.close()
file.close()
