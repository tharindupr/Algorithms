comp=input()
count=0
li=['A','D','X','Y','P','R']
dic={'A':0,'D':0,'X':0,'Y':0,'P':0,'R':0}
for i in comp:
     if(i=='A'):
          dic['A']=dic['A']+1
     elif(i=='D'):
          dic['D']=dic['D']+1
     elif(i=='X'):
          dic['X']=dic['X']+1
     elif(i=='Y'):
          dic['Y']=dic['Y']+1
     elif(i=='P'):
          dic['P']=dic['P']+1
     elif(i=='R'):
          dic['R']=dic['R']+1
     


     
mincomp=min(dic, key=dic.get)
print(dic[mincomp])
