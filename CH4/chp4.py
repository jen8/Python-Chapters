def area_of_circle(r):
    area = (3.14)*r**2
    return area

print (area_of_circle(2))

def is_divisible_by_n (money, ticketCost):
    if money % ticketCost == 0:
        print "Yes,", money, "is divisible by", ticketCost
        
    else:
        print "No,", money, "is not divisible by", ticketCost

def sum_to(n):
    sum = 0
    for num in range(n + 1):
        sum = sum + num
    return sum
  
def sum_to2(n):
    sum = 0
    num = 0
    while num < n + 1:
        sum = sum + num
        num = num + 1
    return sum  
        
print (sum_to(10))
print (sum_to2(10))

def dispatch (choice):
    
    if choice == 'a':
        function_a()
    
    elif choice == 'b':
        function_b()

    elif choice == 'c':
        function_c()
            
    else:
        print "Invalid choice."


def function_a():
    print "function_a was called..."
    
def function_b():
    print "function_b was called..."
    
def function_c():
    print "function_c was called..."
    
def compare (x, y):

    if x < y:
        print x, "is less than", y
    elif x > y:
        print x, "is greater than", y
    else:
        print x, "and", y, "are equal"
    
compare (2, 3)
compare (5, 4)
compare (7, 7)
    