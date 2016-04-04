def exam_grade(score):
    if score >= 75:
        return ("First")
    elif score >= 70 and score < 75:
        return ("Upper Second")
    elif score >= 60: 
        return ("Second")
    elif score >= 50:
        return ("Third")
    elif score >= 45:
        return ("F1 Supp")
    elif score >= 40:
        return ("F2")
    else:
        return ("F3")
          
xs = [83, 75, 74.9, 70, 69.9, 65, 60, 59.9, 55, 50, 49.9, 45, 44.9, 40, 39.9, 2, 0]

for score in xs:
    print (score, exam_grade(score))

#def find_hypot(a,b):
#    hypotenuse = (a**2 + b**2)**0.5
#    return hypotenuse

#print (find_hypot(3,4))

#def is_rightangled(a,b,c):
#    if c**2 == (a**2 + b**2):
#        return True
#    else:
#        return False
    
#print (is_rightangled(3,4,5))

#import math
#a = math.sqrt(2.0)
#print(a, a*a)
#print(a*a == 2.0)


def is_rightangled_2(a,b,c):
    if a > c and a > b:
        hypotenuse = a
        a = c
    elif b > c and b > a:
        hypotenuse = b
        b = c       
    else:
        hypotenuse = c
        
    if hypotenuse**2 == (a**2 + b**2):
        return True
    else:
        return False

x = is_rightangled_2(3,4,5)
print (is_rightangled_2(2,3,4))
return (x)   
print (is_rightangled_2(5,4,3))     
    
    