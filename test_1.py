"""
We are going to determine whether if
option_1: Pays $100 per day 
or 
option_2: pays $1 first day then it doubles everyday for ten days
is better 
if option_1 pays more then display: Option 1 is better 
else 
if option_2 is pays more then display: Option 2 is better
if both options equal the same amount then both 
we will display option_1 and option_2 pay the same amount. 

"""

"""
option_1 = 
    100 * 10 

option_2 = 
    amount = 1
    days = []
    loop the amount 10 times 
    times the amount by 2
total = sum(days)
return the total amount

result
    if option_1 == option_2
        display both options pay the same amount
    if option_1 > option_2 
        display option_1 is better 
    if option 2 > option_1 
        display option_2 is better
    
"""


def option_1():
    return 100 * 10 

def option_2():
    option_2_amount = 1
    list_of_days = []
    for i in range(0, 10):
        list_of_days.append(option_2_amount)
        option_2_amount *= 2
    total = sum(list_of_days)
    return total

def result():
    answer = ""
    var_1 = option_1()
    var_2 = option_2()
    if var_1 == var_2: 
        answer = "Option 1 and Option pay the same amount."
    elif var_1 > var_2:
        answer = "Option 1 pays more than option 2 thus it is better."
    else:
        answer = "Option 2 pays more than option 1 thus it pays better"
    print(answer)

result()
