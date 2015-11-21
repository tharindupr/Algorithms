z=int(input())
for j in range(z):
    n=int(input())
    li=raw_input().split(' ')
    comp=[]

    def find(li,e):
        for i in range(len(li)):
            if e in li[i]:
                return(i)
            
        return(-1)

    for i in range(n):

        a=find(comp,str(i+1))
        b=find(comp,li[i])
        if(a>=0 or b>=0):
            comp[max(a,b)].append(str(i))
            comp[max(a,b)].append(li[i])
        else:
            comp.append([str(i+1),li[i]])

        
        
    print(len(comp)-1)
