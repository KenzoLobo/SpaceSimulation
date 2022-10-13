# A Black_Hole is derived from a Simulton base; it updates by finding+removing
#   any objects (derived from a Prey base) whose center is crosses inside its
#   radius (and returns a set of all eaten simultons); it displays as a black
#   circle with a radius of 10 (e.g., a width/height 20).
# Calling get_dimension for the width/height (for containment and displaying)'
#   will facilitate inheritance in Pulsator and Hunter

from simulton import Simulton
from prey import Prey
import math

class Black_Hole(Simulton):  
    radius=10
    def __init__(self,x,y,width,height):
        Simulton.__init__(self,x,y,width,height)
        
    def update(self,model):
        eaten=model.find(self.contains)
        model.simuls=model.simuls-eaten
        return eaten
    
    def display(self,canvas):
       canvas.create_oval(self._x-self.radius      , self._y-self.radius,
                                self._x+self.radius, self._y+self.radius,
                                fill="black")
    def contains(self,xy):
        dist=Simulton.distance(self,xy)
        if dist<self.radius:
            return True 
        else:
            return False
