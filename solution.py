# Check if point is inside circle, consider edge case as separate
def isInCircle(r, x, y):
     if((x*x + y*y) < r*r): 
         return 1 	# Point inside circle
     if((x*x + y*y) == r*r): 
         return 2 	# Point on edge
     return 3		# Point outside circle

# Check if point is in ring, first check inner circle, then outer
def isInRing(inner, outer, x, y):
     if(isInCircle(inner, x, y) == 3):
         if(isInCircle(outer, x, y) == 1):
             return True
     return False

def solution(inner, outer, points_x, points_y):
     cnt = 0
     for i in range(0,len(points_x)):
         if(isInRing(inner,outer,points_x[i],points_y[i])):
             cnt+=1
     return cnt

