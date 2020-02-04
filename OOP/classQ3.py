class Segment(object):
    def __init__(self, x0=0, x1=0, color="blue"):
        self._x0 = x0
        self._x1 = x1
        self._color = color

    def left(self):
        return self._x0
    
    def right(self):
        return self._x1
    
    def get_color(self):
        return self.color
        
    def set_color(self,color):
        self.color = color

    def mid_point(self):
        return ((int(self._x0) + int(self._x1)) // 2)

    def contains(self,num):
        if num in range(self._x0, self._x1):
            return True
        else:
            return False
    
    def overlaps(self,seg):
        if (seg._x1 == self._x1 and seg._x0 ==  self._x0) :
            return True
        else:
            return False 

    def __It__(self,midpoint1,midpoint2):
        if (midpoint1 < midpoint2):
            return "original mid point is less"
        elif (midpoint1 == midpoint2):
            return "both midpoints are same"    
        else:
            return "new mid point is less"
            
    def __str__(self):
        return "[{}---{}]" .format(self._x0,self._x1)

