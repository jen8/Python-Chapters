def count_digits_divis_three(n):
    """
      >>> count_digits_divis_three(3)
      1
      >>> count_digits_divis_three(36)
      2
      >>> count_digits_divis_three(313)
      2
      >>> count_digits_divis_three(111)
      0
      >>> count_digits_divis_three(0)
      0
    """
    count = 0
    while n > 0:
        current_digit = n % 10
        if current_digit % 3 == 0:
            count = count + 1
        n = n / 10
    return count
#print "a:",count_digits_divis_three(319)

def sum_primes(n):
    """
      >>> sum_primes(1)
      1
      >>> sum_primes(3)
      6
      >>> sum_primes(8)
      18
    """
   sum = 0                                  
   current_digit = 1                       
                    
    while current_digit <= n:               
        if is_prime(current_digit):         
            sum = sum + current_digit       
        current_digit += 1
    return sum                              


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
def sum_products(n):
    """
      >>> sum_products(1, 1)
      1
      >>> sum_products(1, 2)
      3
      >>> sum_products(2, 3)
      21
    """
    
def count_sheep(sheep):
    x = 1
    while x < n:
        print x, '\t',
        x +=1
        print 'Sleeping time!'
    
if __name__ == '__main__':
    import doctest
    doctest.testmod()