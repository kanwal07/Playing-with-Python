#Create a class Segement with following functions and also include the testing of all functions
# 1. __init__(): Constructor that takes one or two arguments to build the line segment
# 2. left(): returns the coordinate of the left boundry
# 3. right(): returns the coordinate of the right boundry
# 4. set_color(): sets the color of the segment to red, blue or green
# 5. mid_point(): returns the coordinate of the mid point of the line segment
# 6. contains(): takes a double argument and returns a boolean indicating whether it is in the segment
# 7. overlaps(): takes a segment argument and returns a boolean indicating whether this segment and original segment overlaps.
# 8. __it__(): a "less than" method that compares the midpoints of the segments.
# 9. __str(): returns a string representation of the segment (of the form [x0--x1]) 

from classQ3 import Segment

object1 = Segment(2,3,"blue")
print("The left Coordinate is: " + str(object1.left()))
object1.set_color("green") 
print("New color: "+ str(object1.get_color()))  
print("The mid point: " + str(object1.mid_point()))
print("The line contains 5 or not : " + str(object1.contains(5)))

object2 = Segment(3,3,"red")
print("Does the second line overlaps ?: "+ str(object1.overlaps(object2)))
midpoint1 = object1.mid_point()
midpoint2 = object2.mid_point()

print("less than method: "+ str(object1.__It__(midpoint1,midpoint2)))
print(object1.__str__())