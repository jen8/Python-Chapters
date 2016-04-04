def turn_clockwise(direction):
    if direction == "N":
        return "E"
    elif direction == "E":
        return "S"
    elif direction == "S":
        return "W"
    elif direction == "W":
        return "N"
    else:
        return  

def day_name(day_num):
    if day_num == 0:
        return "Sunday"    
    elif day_num == 1:
        return "Monday"
    elif day_num == 2:
        return "Tuesday"
    elif day_num == 3:
        return "Wednesday"
    elif day_num == 4:
        return "Thursday"
    elif day_num == 5:
        return "Friday"
    elif day_num == 6:
        return "Saturday"
    else:
        return
    
def day_num(day_name):
    if day_name == "Sunday":
        return 0    
    elif day_name == "Monday":
        return 1
    elif day_name == "Tuesday":
        return 2
    elif day_name == "Wednesday":
        return 3
    elif day_name == "Thursday":
        return 4
    elif day_name == "Friday":
        return 5
    elif day_name == "Saturday":
        return 6
    
    else:
        return



def day_add(name_day, delta):

    if name_day == "Sunday":
        day = 0     
    elif name_day == "Monday":
        day = 1   
    elif name_day == "Tuesday":
        day = 2
    elif name_day =="Wednesday":    
        day = 3       
    elif name_day == "Thursday":
        day = 4    
    elif name_day == "Friday":
        day = 5   
    elif name_day == "Saturday":
        day = 6
    else:
        return 

    leave_day = (day + delta) % 7
    return day_name(leave_day)     





def days_in_month(month):
    
    if month == "January": 
        return 31
    
    elif month == "February": 
        return 28
    
    elif month == "March": 
        return 31
    
    elif month == "April": 
        return 30
    
    elif month == "May": 
        return 31
    
    elif month == "June": 
        return 30
    
    elif month == "July": 
        return 31
    
    elif month == "August": 
        return 31
    
    elif month == "September": 
        return 30
    
    elif month == "October": 
        return 31
    
    elif month == "November": 
        return 30
    
    elif month == "December": 
        return 31
    
    else:
        return
    
def to_secs(hours, minutes, seconds):
    hours = hours * 60 * 60 
    minutes = minutes * 60 
    seconds = seconds
    sum = hours + minutes + seconds
    return sum
        

def to_secs2(hours, minutes, seconds):
    hours = int(hours * 60 * 60) 
    minutes = int(minutes * 60) 
    seconds = int(seconds)
    return sum


def hours_in(seconds):
    hours = (seconds/60/60)
    return int(hours)

    
def minutes_in(seconds):
    hours = float(seconds / 60 / 60)
    leftover_hour = hours % int(hours)
    minutes = leftover_hour * 60
    return int(minutes)

def minutes_in2(seconds):
    minutes = seconds // 60 # calculate minutes
    return minutes % 60 # discard hours from minutes


def seconds_in(seconds):
    hours = float(seconds / 60 / 60)
    leftover_hour = hours % int(hours)
    minutes = leftover_hour * 60                    
    leftover_minutes = minutes % int(minutes)   
    seconds = leftover_minutes * 60
    return round(seconds)

def seconds_in2(seconds):
    minutes = float(seconds / 60)                   
    leftover_minutes = minutes % int(minutes)   
    seconds = leftover_minutes * 60
    return round(seconds)    

def seconds_in3(seconds):
    return seconds % 60

def compare(a,b):
    if a > b:
        return 1
    elif a == b:
        return 0
    elif a < b:
        return -1
    else:
        return
    
def hypotenuse (a,b):  
    c = (a**2 + b**2)**0.5        
    return c

def slope(x1,y1,x2,y2):
    slope = (y2 - y1) / (x2 - x1)
    return slope

def intercept(x1,y1,x2,y2):
    y_int = y2 - (slope(x1,y1,x2,y2) * x2)
    return y_int   

def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False

def is_odd(n):
    if n % 2 != 0:
        return True
    else:
        return False
    
def is_odd2(n):
    if is_even(n) == True:
        return False
    else:
        return True

def is_factor(f,n):
    if n % f == 0:
        return True
    else:
        return False

def is_multiple(n,f):

    if is_factor(f,n) == True:
        return True
    else:
        return False

def f2c(F):
    C = round((F - 32) * 5/9)
    return C


def c2f(C):
    F = round((C * 9/5) + 32)
    return F
        
    
    
    
    
    
    


import sys

def test(did_pass):
    """  Print the result of a test.  """
    linenum = sys._getframe(1).f_lineno   
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)
    

def test_suite():
    """ Run the suite of tests for code in this module (this file).
    """
    test(turn_clockwise("N") == "E")
    test(turn_clockwise("W") == "N")
    test(turn_clockwise("42") == None)
    test(turn_clockwise("rubbish") == None)

    test(day_name(3) == "Wednesday")
    test(day_name(6) == "Saturday" )
    test(day_name(42) == None)

    test(day_num("Friday") == 5)
    test(day_num("Sunday") == 0)
    test(day_num(day_name(3)) == 3) 
    test(day_name(day_num("Thursday")) == "Thursday") 
    
    test(day_add("Monday", 4) ==  "Friday")
    test(day_add("Tuesday", 0) == "Tuesday")
    test(day_add("Tuesday", 14) == "Tuesday")
    test(day_add("Tuesday", 6) == "Monday")
    test(day_add("Sunday", 100) == "Tuesday")
    
    test(day_add("Sunday", -1) == "Saturday")
    test(day_add("Sunday", -7) == "Sunday")
    test(day_add("Tuesday", -100) == "Sunday")
        
    test(days_in_month("February") == 28)
    test(days_in_month("December") == 31)
    test(days_in_month("dog") == None)
    
    test(to_secs(2,30,10))
    test(to_secs(2, 0, 0)) 
    test(to_secs(0, 2, 0))
    test(to_secs(0, 0, 42))
    test(to_secs(0, -10, 10))
    
    test(to_secs(2.5, 0, 10.71))
    test(to_secs(2.433,0,0))
            
    test(hours_in(9010) == 2)
    test(minutes_in2(9010) == 30)
    test(seconds_in3(9010) == 10)
    
    test(compare(5, 4) == 1)
    test(compare(7, 7) == 0)
    test(compare(2, 3) == -1)
    test(compare(42, 1) == 1)
    
    test(hypotenuse(3, 4) == 5.0)
    test(hypotenuse(12, 5) == 13.0)
    test(hypotenuse(24, 7) == 25.0)
    test(hypotenuse(9, 12) == 15.0)

    test(slope(5, 3, 4, 2) == 1.0)
    test(slope(1, 2, 3, 2) == 0.0)
    test(slope(1, 2, 3, 3) == 0.5)
    test(slope(2, 4, 1, 2) == 2.0)
    
    test(intercept(1, 6, 3, 12) == 3.0)
    test(intercept(6, 1, 1, 6) == 7.0)
    test(intercept(4, 6, 12, 8) == 5.0)
    
    test(is_even(68) == True)
    test(is_even(2500) == True)
    test(is_even(159) == False)
    test(is_even(9873) == False)
    
    test(is_odd(39) == True)
    test(is_odd(510) == False)
    test(is_odd(793) == True)
    
    test(is_odd2(39) == True)
    test(is_odd2(510) == False)
    test(is_odd2(793) == True)
    
    test(is_factor(3, 12))
    test(not is_factor(5, 12))
    test(is_factor(7, 14))
    test(not is_factor(7, 15))
    test(is_factor(1, 15))
    test(is_factor(15, 15))
    test(not is_factor(25, 15))
    
    test(is_multiple(12, 3))
    test(is_multiple(12, 4))
    test(not is_multiple(12, 5))
    test(is_multiple(12, 6))
    test(not is_multiple(12, 7))
    
    test(f2c(212) == 100)     # Boiling point of water
    test(f2c(32) == 0)        # Freezing point of water
    test(f2c(-40) == -40)     # Wow, what an interesting case!
    test(f2c(36) == 2)
    test(f2c(37) == 3)
    test(f2c(38) == 3)
    test(f2c(39) == 4)
    
    test(c2f(0) == 32)
    test(c2f(100) == 212)
    test(c2f(-40) == -40)
    test(c2f(12) == 54)
    test(c2f(18) == 64)
    test(c2f(-48) == -54)
    

test_suite()        
        
   
