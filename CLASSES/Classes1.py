import math

class Point:
    """ Point class represents and manipulates x,y coords. """

    def __init__(self, x=0, y=0):
        """ Create a new point at the origin """
        self.x = x
        self.y = y
        
    def distance_from_origin(self):
        """ Compute my distance from the origin """
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5
    
    def __str__(self):
        return "({0}, {1})".format(self.x, self.y)

    def halfway(self, target):
        """ Return the halfway point between myself and the target """
        mx = (self.x + target.x)/2
        my = (self.y + target.y)/2
        return Point(mx, my)
    
    def reflect_x(self):
        return Point(self.x, self.y * -1)
    
    def slope_from_origin(self):
        return self.slope_to(Point(0,0))
    
    def get_line_to(self, target): 
        slope = self.slope_to(target)
        slope_int = self.y - (slope * self.x)
        return (slope, slope_int)
    
    def slope_to(self, target):
        return (self.y - target.y) / (self.x - target.x)
    
def distance(p1, p2):
    return math.sqrt( (p2.x-p1.x)**2 + (p2.y-p1.y)**2 )

def circle_midpoint(p1, p2, p3):
    slope_r = p1.slope_to(p2)
    slope_t = p2.slope_to(p3)
    x = (slope_r * slope_t * (p3.y - p1.y) + slope_r * (p2.x + p3.x) - slope_t * (p1.x + p2.x)) / (2 * (slope_r - slope_t))
    y =  (-1/slope_r) * (x - (p1.x + p2.x) / 2) + (p1.y + p2.y) / 2
    return Point(x,y)

print (circle_midpoint(Point(5,5), Point(6,-2), Point(2, -4)))
print (circle_midpoint(Point(1,1), Point(2,4), Point(5,3)))

print (distance(Point(1, 2), Point(4, 6)))
    
p = Point(3,4)         # Instantiate an object of type Point
q = Point(5,12)         # Instantiate second object of type Point
r = p.halfway(q) 

print (p.reflect_x())
print(Point(4,10).slope_from_origin())
print(Point(4, 11).get_line_to(Point(6, 15)))

print(p.x,p.y,p.distance_from_origin())
print(q.x,q.y,q.distance_from_origin())
print(r.x,r.y,r.distance_from_origin())   # Each point object has its own x, y, and r
print(p,q,r)
print(Point(3, 4).halfway(Point(5, 12)))
