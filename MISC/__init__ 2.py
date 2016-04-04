#import sys 

# Print out 3 options
# Read string from console
# do switch-case with input and print Siri things

print "Khloe here, your personal Python interpreter..."

s = '1'
while s != '9':

    print "What can I do for you?"
    print "1) Make me a sandwich"
    print "2) How do I get to Mars"
    print "3) You belong in the kitchen"
    print "9) Turn off Khloe "
    
    s = raw_input('--> ')
    if s == '1':
      print("If you say so")
    elif s =='2':
      print("You fly there genius")
    elif s == '3':
      print("I am not permitted to cook")
    elif s == '9':
      pass
    else:
      print("Please speak English please")

    print("")

#input "if you say so"
#break means case ends here, dont print the next case
#default is the default statement that prints when none of the cases are valid