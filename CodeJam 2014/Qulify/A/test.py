a=int(input())
b=int(input())
k=int(input())

alist=[]
blist=[]
klist=[]

for i in range(0,a):
    alist.append(i)
for j in range(0,b):
    blist.append(j)
for l in range(0,k):
    klist.append(l)

count=0
for x in alist:
    for y in blist:
        if(x&y) in klist:
            count+=1
print(count)
