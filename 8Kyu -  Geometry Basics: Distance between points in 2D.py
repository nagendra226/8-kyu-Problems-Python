import math
def distance_between_points(a, b):
    # your code here
    x1 = a.x
    y1 = a.y
    x2 = b.x
    y2 = b.y
    return math.sqrt((x1-x2)**2+(y1-y2)**2)
    
