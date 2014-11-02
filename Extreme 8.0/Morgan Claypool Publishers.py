case = list(map(int,input().split()))# create a list of Integer from a list of String
subjects=case[0]
num_of_constraints=case[1]

constraints=[]
for x in range(num_of_constraints): # get constraints and put them in a list
    constraints.append(list(map(int,input().split())))

unique=set(constraints[0]) # take 1st record and put them in set

for recrd in constraints[1:]: #create a list of all unique numbers in constraints
    '''1 3, 1 5, 3 5 will be formatted as 1,3,5'''
    unique |=set(recrd)
plan = list(map(int,input().split()))

state=True
if(not (len(unique) == len(plan))): # if the number of subjects differ than given constraints
    state=False
else:
    for x in constraints: # We check weather order in the constraints are also same in the given plan
        '''As a example consider constraint 1 3
            plan is 1 5 3 4.
            the index of 1 is lower than index of 3.
            If not we set state as False'''
        if plan.index(x[0])>plan.index(x[1]):
            state=False
            break

out="YES" if state else "NO"
print(out)