limit=int(input())
sent=input()
words=sent.split(" ")
l=[]
for x in words:
     l.append(len(x))



     
def tablecal(table,limit):
     t=matrix(len(table),len(table))
     for i in range (0,len(table)):
          
          for j in range(0,len(table)):
               if(i<=j):
                    error=sum(table[i:j+1])+len(table[i:j+1])-1
                    if(error<=limit):
                         t.table[i][j]=((limit-error)**3)
                         
     return(t)            


         
                    
          

class matrix:
     def __init__(self,x,y):
          self.table=[]
          for i in range(x):
               self.table.append([])
               for j in range(y):
                    self.table[i].append("")
          

table1=tablecal(l,limit).table
c=[0]
lis=[]
for k in range(1,len(l)+1):
     c.append("inf")
     for j in range(1,k+1):
          if(c[j-1]!="inf" and table1[j-1][k-1]!="" and (table1[j-1] + table1[j-1][k-1] < c[k]) ):
               #lis.append(c[j-1]+table1[j-1][k-1])
               c[k]=c[j-1] + table1[j-1][k-1]
     #c.append(min(lis))
     lis=[]
     
               
print(c[len(c)-1])               
          
