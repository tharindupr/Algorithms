def val(innitvar,basevar,convertvar):
     #innitvar = input("Please enter a number: ")
     #basevar = int(input("Please enter the base that your number is in: "))
     #convertvar = int(input("Please enter the base that you would like to convert to: "))

     # Create a symbol-to-value table.
     SY2VA = {'0': 0,
              '1': 1,
              '2': 2,
              '3': 3,
              '4': 4,
              '5': 5,
              '6': 6,
              '7': 7,
              '8': 8,
              '9': 9,
              'a': 10,
              'b': 11,
              'c': 12,
              'd': 13,
              'e': 14,
              'f': 15,
              'g': 16,
              'h': 17,
              'i': 18,
              'j': 19,
              'k': 20,
              'l': 21,
              'm': 22,
              'n': 23,
              'o': 24,
              'p': 25,
              'q': 26,
              'r': 27,
              's': 28,
              't': 29,
              'u': 30,
              'v': 31,
              'w': 32,
              'x': 33,
              'y': 34,
              'z': 35,}

    

     integer = 0
     for character in innitvar:
         assert character in SY2VA, 'Found unknown character!'
         value = SY2VA[character]
         assert value < basevar, 'Found digit outside base!'
         integer *= basevar
         integer += value

     # Create a value-to-symbol table.
     VA2SY = dict(map(reversed, SY2VA.items()))

     
     array = []
     while integer:
         integer, value = divmod(integer, convertvar)
         array.append(VA2SY[value])
     answer = ''.join(reversed(array))

     # Display the results of the calculations.
     return(answer)


inp=input()
numbers=[0,1,2,3,4,5,6,7,8,9]

no=""
memo={}
count=1
for i in inp:
     try:
          no=no+str(memo[i])
     
          
     except:
          if(count==1):
               no=no+str(1)
               count+=1
               memo[i]=1
          else:
               if(0 in memo.values()):
                    no=no+str(count)
                    memo[i]=count
                    count+=1
                    
               else:
                    no=no+str(0)
                    memo[i]=0
                    
l=[]
for x in no:
     l.append(int(x))
     
print(val(no,max(l)+1,10))     
          








