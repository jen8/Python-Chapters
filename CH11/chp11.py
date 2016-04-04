#def add_vectors(u,v):
#    list = [ ]
    
#    sum_1 = u[0] + v[0]
#    list.append(sum_1)
#    sum_2 = u[1] + v[1]
#    list.append(sum_2)
#    if len(u) == 3:
#        sum_3 = u[2] + v[2]
#        list.append(sum_3)
    
#    return list
    
#def add_vectors(u,v):
#    list = [ ]
#    index = 0
    
#    while len(u) > 0:
#        sum = u[index] + v[index]
#        list.append(sum)
#        index += 1
        
#    return list

def scalar_mult(s,v):
    list = [ ]
    index = 0
    for int in v:
        product = v[index] * s
        list.append(product) 
        index += 1
    return list

def dot_product(u,v):
    index = 0
    sum_of_products = 0
    for int in u:
        product = u[index] * v[index]
        sum_of_products = sum_of_products + product
        index += 1        
    return sum_of_products


def replace(s, old, new):
    glue = new
    old_str = s.split(old)
    new_str = glue.join(old_str)
    return new_str


def swap(x, y):      # Incorrect version
    print("before swap statement: x:", x, "y:", y)
    (x, y) = (y, x)
    print("after swap statement: x:", x, "y:", y)

    a = ["This", "is", "fun"]
    b = [2,3,4]
    print("before swap function call: a:", a, "b:", b)
    swap(a, b)
    print("after swap function call: a:", a, "b:", b)


    

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

#    test(add_vectors([1, 1], [1, 1]) == [2, 2])
#    test(add_vectors([1, 2], [1, 4]) == [2, 6])
#    test(add_vectors([1, 2, 1], [1, 4, 3]) == [2, 6, 4])
    
    test(scalar_mult(5, [1, 2]) == [5, 10])
    test(scalar_mult(3, [1, 0, -1]) == [3, 0, -3])
    test(scalar_mult(7, [3, 0, 5, 11, 2]) == [21, 0, 35, 77, 14])
    
    test(dot_product([1, 1], [1, 1]) ==  2)
    test(dot_product([1, 2], [1, 4]) ==  9)
    test(dot_product([1, 2, 1], [1, 4, 3]) == 12)
    
    
    test(replace("Mississippi", "i", "I") == "MIssIssIppI")
    
    s = "I love spom! Spom is my favorite food. Spom, spom, yum!"
    test(replace(s, "om", "am") ==
        "I love spam! Spam is my favorite food. Spam, spam, yum!")
    
    test(replace(s, "o", "a") ==
        "I lave spam! Spam is my favarite faad. Spam, spam, yum!")







test_suite()