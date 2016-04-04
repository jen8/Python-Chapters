def num_odd_digits(n):
    """
      >>> num_odd_digits(1234567)
      2
      >>> num_odd_digits(2468)
      0
      >>> num_odd_digits(1357)
      4
      >>> num_odd_digits(1)
      1
      >>> num_odd_digits(31)
      2
    """
    count = 0
    
    while n:
        if n % 2 != 0:
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
    
    n = n / 10
    print n
    
    
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
    
    current_digit = n
    sum = 0
    
    while n:
        current_digit = current_digit**2
        sum = sum + current_digit
        n = n / 10
    return sum
    
    
