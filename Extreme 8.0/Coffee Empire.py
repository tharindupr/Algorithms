'''We are maintaining a Corner object for each corner
   After filling data we calculate income for each corner and 
   put them in a 2D list. Then we find the maximum value out of them and 
   print its' coordinates'''

class Corner:

    def __init__(self):
        self.days={} # holds income for each day "{Monday:10, Tuesday:0, ...}"
        self.benefited_Days={} # holds weather day has a income over $5 "{Monday:True, Tuesday:False, ...}"
        self.num_shops=0 # Count of the shops in this corner
        self.has_3=False # Weather a corner has 3 shops or not
        self.offered_benefit=0 # holds the benefit that offers to its' adjacent corners in a week

    def set_daily_income(self,day,income ):
        self.days[day]=income
        if(income>=5):
            self.benefited_Days[day]=True
        else:
            self.benefited_Days[day]=False

    def set_num_shops(self,num): 
        self.num_shops=num
        if(num==3):
            self.has_3=True

    def has_3_shops(self):
        return self.has_3

    def get_relative_income(self): # income of a corner is
        value=0
        for day in self.days:
            value +=self.days[day]/(self.num_shops+1)
        return value

    def set_weekly_benefit(self):
        if(self.has_3):
            for day in self.benefited_Days:
                if(self.benefited_Days[day]): #is True or False
                    self.offered_benefit +=1


    def get_weekly_benefit(self):
        return self.offered_benefit
'''End of Class definition'''

'''Fetching input data '''
def set_shops(shop_layout,row):
    for corner, num_of_shops in  enumerate(shop_layout): # enumerate returns both index and value of a list element
        if(num_of_shops=='H'):
            row[corner].set_num_shops(3)
        elif(num_of_shops=='M'):
            row[corner].set_num_shops(2)
        elif(num_of_shops=='L'):
            row[corner].set_num_shops(1)

case=list(map(int,input().split())) # create a list of Integer from a list of String
width=case[0]
height=case[1]
corner_grid=[]     #Holds Corner objects
'''0th index of corner_grid contains a list of Corner objects which 
   represent the 1st row of corners'''

'''Read initializing lines of input and create a 2D list of Corner objects'''
for x in range(height):
    row=[Corner() for y in range(width)] #genarate a list of 'Corner' objects based on width
    shop_layout=input().split('*')
    set_shops(shop_layout,row) # fill data about shops in Corner objects
    corner_grid.append(row)

'''set income of day for every corner in the current row by day'''
def set_income_of_day(traffic_layout,row,day):
        for corner, traffic in enumerate(traffic_layout):
            row[corner].set_daily_income(day,traffic)

'''Since we have 7 days, we add all the data about traffic of particular corner to the relevant Corner object '''
for x in range(7):
    day = input() # read day
    for row_index in range(height): # Read data about traffic in each corner within a day
        traffic_layout=list(map(int,input().split('*')))
        '''passing traffic information, list of corner objects and current day'''
        set_income_of_day(traffic_layout,corner_grid[row_index],day)

'''All data filled'''

'''Processing Data'''

'''A corner can be beneficial to its' adjacent corners if that corner has 3 shops and
    has a income of $5 or greater for a given day.
    Number of shops for a given corner does not change over time, but income varies from day to day
    So a corner may be beneficial to its' adjacent corners only in some days.
    What we do here is take a corner, check whether it has 3 shops or not.
    if it has 3 shops:
        {check whether it has a income over $5 for a given day
        if it has, then increase the 'offered_benefit' variable by one
        }
        this block will be executed for all seven days
    After execution of this method 'set_weekly_benefit()', we can get the benefit of a corner by
    calling 'get_weekly_benefit()' method '''

for x in corner_grid:
    for i in x:
        i.set_weekly_benefit()

'''get benefit from a adjacent corner'''
def check_up(row_num,corner_num):
    if (row_num-1>=0): # if it has a row above get its' benefit
        return corner_grid[row_num-1][corner_num].get_weekly_benefit()
    else:               # if it does not have a row above return 0
        return 0

def check_down(row_index,corner_num):
    if(len(corner_grid)>row_index+1):
        return  corner_grid[row_index+1][corner_num].get_weekly_benefit()
    else:
        return 0

def check_left(row_num,corner_num):
    if(corner_num-1>=0):
        return corner_grid[row_num][corner_num-1].get_weekly_benefit()
    else:
        return 0

def check_right(row_num,corner_num):
    if(corner_num+1<width):
        return corner_grid[row_num][corner_num+1].get_weekly_benefit()
    else:
        return 0

income_grid=[]
'''Calculate income for all corners and put them in a 2D grid similar to the corner grid'''
for row_index,row in enumerate(corner_grid):
    income_row=[]
    for corner_num,corner in enumerate(row):
        '''If a corner has 3 shops we cannot place our shop there, so there will be no income if we place
            our shop there'''
        if(not corner.has_3_shops()):
            up_benefit=check_up(row_index,corner_num)
            down_benefit=check_down(row_index,corner_num)
            left_benefit=check_left(row_index,corner_num)
            right_benefit=check_right(row_index,corner_num)
            traffic_income=corner.get_relative_income()

            income_row.append(up_benefit + down_benefit + left_benefit + right_benefit + traffic_income)
        else:
            income_row.append(0)
    income_grid.append(income_row)

max_income=[] # holds the max income of each row
for row in income_grid:
    max_income.append(max(row)) #max val of 0th row will be added to the 0th index of max_income list

max_of_all=max(max_income) # get max income out of all rows

if(max_of_all>=20):
    Y=row_indx_of_grid = max_income.index(max_of_all) # get index of row which holds the max_of_all ->(y)
    X=income_grid[row_indx_of_grid].index(max_of_all) # find the index of max_of_all in selected row ->(X)
    print(X+1,Y+1)
else:
    print(-1,-1)

