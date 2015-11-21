f=open("A-small-attempt1.in",'r')
t=int(f.readline().strip())
for j in range(t):
     case=f.readline().strip().split(" ")

     friends=0
     pre=0
     count=0
     for i in case[1]:
          if(pre<count):
               friends+=count-pre
          pre+=friends
          pre=pre+int(i)
          count+=1

     print("Case #"+str(j+1)+": "+str(friends))
          
     
     
