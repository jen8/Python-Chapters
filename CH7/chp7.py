#def sum(n):
#    ss = 0
#    v = 1
#    while v < n:
#        ss = ss + v
#        v = v + 1
#    return ss



grades = [5, 2, 9, 200, 53, 400, 150, 99 ]

def odd_numbers(list):
    count = 0
    for num in list:
        if num % 2 != 0:
            count +=1
    return count


def sum_even(list):
    sum = 0
    for num in list:
        if num % 2 == 0:
            sum = sum + num
    return sum



def sum_of_negative_num(list):
    sum = 0
    for num in list:
        if num < 0:
            sum = sum + num
    return sum


def length_five(list):
    count = 0
    for num in list:
        if len(num) == 5:
            count +=1
    return count


def sum_up_to_first_even_num(list):
    sum = 0
    for num in list:
        if num % 2 == 0:
            break 
        sum = sum + num
                
    return sum

def sum_up_to_first_even_num_2(list):
    sum = 0    
    for num in list:
        if num % 2 == 0:
            return sum
        else:
            sum = sum + num                
    return sum


# ANSWER: if there aren't any even numbers in the list, then the function just takes the sum of all odd numbers in the list


def sum(n):
    ss = 0
    for num in range(n+1):
        ss = ss + num
    return ss


def sum2(n):
    ss = 0
    v = 1
    while v <= n:
        ss = ss + v
        v = v + 1
        
    return ss


def sum_words_up_to_sam(list):
    count = 0
    for name in list:
        count +=1
        if name == "Sam":
            break
    return count

def sum_words_up_to_sam_2(list):
    count = 0
    for name in list:
        count +=1
        if name == "Sam":
            return count
    return count


# ANSWER : If there aren't any "Sam" names within the list, the function just prints out all items in the list.

def sqrt(n):
    approx = n/2.0     # Start with some or other guess at the answer
    while True:
        better = (approx + n/approx)/2.0
        print (better)
        if abs(approx - better) < 0.001:
            return better
        approx = better


#print(sqrt(25))

# ANSWER: The console (on Eclipse)  continually prints "5.0" continuously. But the terminal print out "7.25"..Why??

#def print_mult_table(high):
#    for i in range(1, high+1):
#        print_multiples(i, high)

# still need to trace this program

def print_triangular_num(n):
    if n == 1:
        print (1)    
    for i in range(1, n + 1):
        result = (i * (i + 1)) / 2
        print(i, "\t", int(result))
print (print_triangular_num(5))



def is_prime(n):
    for num in range(2,n):
        if n % num == 0:
            return False
    return True
    
    
def num_digits(n):
    count = 0
    if n < 0:
        n = n * -1
    if n == 0:
        return 1
    while n > 0:
        count +=1
        n = n // 10
    return count


    
def num_even_digits(n):
    if n == 0:
        return 1 
    count = 0
    digit = n % 10
    while n > 0:
        digit = n % 10               
        if digit % 2 == 0:
            count +=1
        n = n // 10
    return count


def sum_of_squares(xs):
    sum = 0
    for num in xs:
        sum = sum + num**2 
    return sum


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
    srt = sqrt(25.0)
    test(srt >= 4.999 and srt <= 5.001)
    
    test(odd_numbers(grades) == 4)
    
    test(sum_even(grades) == 752)
    
    test(sum_of_negative_num([-7, 8, -22, 10, -3, 19, -2]) == -34)
    
    test(length_five(["un", "deux", "trois", "quatre", "cinq"]) == 1)
    
    test(sum_up_to_first_even_num(grades) == 5)
    test(sum_up_to_first_even_num([3 ,6, 9, 4]) == 3 )
    test(sum_up_to_first_even_num([5, 9, 7, 11]) == 32)
    
    test(sum_up_to_first_even_num_2(grades) == 5)
    test(sum_up_to_first_even_num_2([3 ,6, 9, 4]) == 3 )
    test(sum_up_to_first_even_num_2([5, 9, 7, 11]) == 32)
    
    test(sum(5) == 15)
    test(sum2(5) == 15)
    
    test(sum_words_up_to_sam(["Bob", "Greg", "David", "Suzanne", "Sam", "Rebecca", "Laquisha"]) == 5)
    test(sum_words_up_to_sam(["Bob", "Greg", "David", "Ryan", "Suzanne", "Sam", "Rebecca", "Laquisha"]) == 6)
    test(sum_words_up_to_sam(["Bob", "Rebecca", "Laquisha"]) == 3)
    
    test(sum_words_up_to_sam_2(["Bob", "Greg", "David", "Suzanne", "Sam", "Rebecca", "Laquisha"]) == 5)
    test(sum_words_up_to_sam_2(["Bob", "Greg", "David", "Ryan", "Suzanne", "Sam", "Rebecca", "Laquisha"]) == 6)
    test(sum_words_up_to_sam_2(["Bob", "Rebecca", "Laquisha"]) == 3)
    
    test(is_prime(11))
    test(not is_prime(35))
    test(is_prime(19911121))
    test(not is_prime(19860302))
    
               
    test(num_digits(12345) == 5)
    test(num_digits(0) == 1)
    test(num_digits(-12345) == 5)
    
           
    test(num_even_digits(123456) == 3)
    test(num_even_digits(2468) == 4)
    test(num_even_digits(1357) == 0)
    test(num_even_digits(12056) == 3)
    test(num_even_digits(0) == 1)
    
    
    test(sum_of_squares([2, 3, 4]) == 29)
    test(sum_of_squares([ ]) == 0)
    test(sum_of_squares([2, -3, 4]) == 29)


test_suite()



# Your friend will complete this function
def play_once(human_plays_first):
    """
       Must play one round of the game. If the parameter
       is True, the human gets to play first, else the
       computer gets to play first.  When the round ends,
       the return value of the function is one of
       -1 (human wins),  0 (game drawn),   1 (computer wins).
    """
    # This is all dummy scaffolding code right at the moment...
    import random                  # See Modules chapter ...
    rng = random.Random()
    # Pick a random result between -1 and 1.
    result = rng.randrange(-1,2)
    print("Human plays first={0},  winner={1} "
                       .format(human_plays_first, result))
    return result

def game():

    choice = True
    comp_wins = 0
    your_wins = 0
    num_draws = 0
    who_goes_first = True
    
    while choice:
        who_goes_first = not who_goes_first
        score = play_once(who_goes_first)
    
        if score == -1:
            print ("You Win!")
            your_wins += 1
        elif score == 0:
            print ("Game Drawn!")
            num_draws += 1        
        else:
            print ("I Win!")
            comp_wins += 1
        
        print("Human has {0} wins, Computer has {1} wins, {2} Game draws"
                           .format(your_wins, comp_wins, num_draws))
        
        total_games = comp_wins + your_wins + num_draws
        percentage = (your_wins / total_games) * 100
        print ("You have {0:.2f}% wins!".format(percentage))
        
       
        play_again = "llgfd"
        while play_again != "yes" and play_again != "no":
            
            play_again = input("Do you want to play again?").lower()
            if play_again == "yes":
                choice = True
            elif play_again == "no":
                choice = False 
            else:
                print("Please give a yes or no answer.")
    
    print ("Goodbye!")

def print_multiples(n, high):
    for i in range(1, high+1):
        print(n * i, end="   ")
    print()

def print_mult_table(high):
    for i in range(1, high+1):
        print_multiples(i, i)
        
#print_mult_table(7)



    



