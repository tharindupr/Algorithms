f=open("A-large-practice.in",'r')
f2=open("output.txt","w")
cases=int(f.readline()[:-1])
count=0
while (count<cases):
    total=0
    v3=[]
    v4=[]
    n=int(f.readline()[:-1])
    v1=(f.readline()[:-1]).split(" ")
    v2=(f.readline()[:-1]).split(" ")
    c=0
    for x in v1:
        v3.append(int(x))
        v4.append(int(v2[c]))
        c+=1
        
    
    v3.sort()
    v4.sort()
    v4.reverse()
    c=0
    for i in v3:
        total=total+i*v4[c]
        c+=1
    count+=1

    f2.write("Case #"+str(count)+": "+str(total)+"\n")

f.close()
f2.close()
