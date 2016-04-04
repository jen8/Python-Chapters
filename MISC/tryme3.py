# function definitions must appear before function is executed
    
def three_lines():
    new_line()
    new_line()
    new_line()
    
def new_line():
    print    

def nine_lines():
    three_lines()
    three_lines()
    three_lines()
    

def clear_screen():
    nine_lines()
    nine_lines()
    three_lines()
    three_lines()
    new_line()
    
        

print "First Line"    
clear_screen()
print "Second Line"

