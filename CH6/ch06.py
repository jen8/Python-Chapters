# print "produces\nthis\noutput."




def sqrt(n):
    approx = n/2.0
    better = (approx + n/approx)/2.0
    while better != approx:
        print better
        approx = better
        better = (approx + n/approx)/2.0
    return approx

#print sqrt(25)

def print_multiples(n):
    i = 1
    while i <= 6:
        print n * i, '\t',
        i += 1
    print
    
    
def print_mult_table():
    i = 1
    while i <= 6:
        print_multiples(i)
        i += 1


def print_triangular_numbers(n):
    x = 1
    var = 1
    while x <= n:
        print (x, "\t", var)
        x += 1
        var += x


def is_prime(n):
    """
      >>> is_prime(5)
      True
      >>> is_prime(6)
      False
      >>> is_prime(7)
      True
    """    
    i = 2
    while i <= n - 1:
        if n % i == 0:
            return False
        i += 1
    return True    

if __name__ == '__main__':   
    import doctest
    doctest.testmod()
    
    
def num_digits(n):
    """
      >>> num_digits(12345)
      5
      >>> num_digits(0)
      1
      >>> num_digits(-12345)
      5
    """
    if n == 0:
        return 1
    if n < 0:
        n = n * (-1)
    
    count = 0
    while n:
        count = count + 1
        n = n / 10
    return count
  
   
def num_even_digits(n):
    """
      >>> num_even_digits(123456)
      3
      >>> num_even_digits(2468)
      4
      >>> num_even_digits(1357)
      0
      >>> num_even_digits(2)
      1
      >>> num_even_digits(20)
      2
    """
    if n == 0:
        return 1
    if n < 0:
        n = n * (-1)
    
    count = 0
    while n:
        current_digit = n % 10
        if current_digit % 2 == 0:
            count = count + 1
        n = n / 10
    return count
    
    
def print_digits(n):
    """
      >>> print_digits(13789)
      9 8 7 3 1
      >>> print_digits(39874613)
      3 1 6 4 7 8 9 3
      >>> print_digits(213141)
      1 4 1 3 1 2
     """
    if n == 0:
        print 0,
   
    while n:
        current_digit = n % 10
        print current_digit,
        n = n / 10
    print
   
  
def sum_of_squares_of_digits(n):
    """
      >>> sum_of_squares_of_digits(1)
      1
      >>> sum_of_squares_of_digits(9)
      81
      >>> sum_of_squares_of_digits(11)
      2
      >>> sum_of_squares_of_digits(121)
      6
      >>> sum_of_squares_of_digits(987)
      194
    """
    if n == 0:
        return 0
    
    sum = 0
    while n:
        current_digit = n % 10
        sum = sum + current_digit**2
        n = n / 10
    return sum

def countdown(n):
    while n > 0:
        print n
        n = n-1
    print "Blastoff!"
    
    
countdown(7)

def blah():
    x = 1
    while x < 13:
        print x, '\t', 2**x
        x += 1
blah()


