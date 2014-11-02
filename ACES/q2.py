def suggest(dic):
     keypad=[[],['a','b','c'],['d','e','f'],['g','h','i'],['j','k','l'],['m','n','o'],['p','q','r','s'],['t','u','v'],['w','z','y','z'],['spc']]
     numbers = {65: 2, 66: 2,67:2,68:3,69:3,70:3,71:4,72:4,73:4,74:5,75:5,76:5,77:6,78:6,79:6,80:7,81:7,82:7,83:7,84:8,85:8,86:8,87:9,89:9,90:9,88:9}
     val=''
     for word in dic:
          for i in word:
               #print(i)
               #print(numbers[ord(i.upper())])
               val=val+str(numbers[ord(i.upper())])
               
     return(val)   


def give(number,dic):
     answ=[]
     for a in dic:
          if(dic[a]==number):
               answ.append(a)
     return(answ)          


def sort(list1,list2):
     l=[]
     for i in list2:
          if(i in list1):
               l.append(i)
               
               
     
          
         
          
     return(l)


dic=[]
while(True):
     try:
          line=input()
     except:
          break
     line=line.strip()
     dic.append(line)
     if(line=="#"):
          break

     
    
dic.append(input())
     


suggestions={}
for a in dic[0:-2]:
     
     suggestions[a]=(suggest(a))
     

code=dic[-1]
codess=code.split("0")
codes=[]
for o in codess:
     if(o!=''):
          codes.append(o)


result=[]
for x in codes:
     
     if(x!=''):
          
          result.append(give(x,suggestions))
out=""
count=0
for i in result:
     
     word=""
     if(len(i)>1):
          i=sort(i,dic)
          word=word+'['
          no=1
          for j in i:
               
               if(no==len(i)):
                    word=word+j+']'
               else:
                    word=word+j+'|'
          
               
               no+=1
     
     elif(len(i)==1):
          word=word+i[0]
     else:
          word="*"*len(codes[count])
     if(count!=len(result)):
          out=out+word+" "
     count+=1    
          
print(out)          
          
     
          
          


#numbers = {65: 2, 66: 2,67:2,68:3,69:3,70:3,71:4,72:4,73:4,74:5,75:5,76:5,77:6,78:6,79:6,80:7,81:7,82:7,82:7,84:8,85:8,86:8,87:9,89:9,90:9}

    
          


