p = 10000
n = 12
r = 0.08
t = int(input("How many years? "))
a = p * (1 + r/n)**(n*t)
print("After", t, "years your", p, "dollars becomes", a)

#def calc_interest(p, r, t):
#    n = 12
#    return p * (1 + r/n)**(n*t)