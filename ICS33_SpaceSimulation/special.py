# Any Prey that comes in contact with a Special
# beomes bigger and faster
from blackhole import Black_Hole
from simulton import Simulton
from prey import Prey
class Special(Black_Hole):
    radius=15
    change=5
    def __init__(self,x,y,width,height):
        Black_Hole.__init__(self,x,y,width,height)
    
    def update(self,model):
        contacted=model.find(self.contains)
        for s in contacted:
            s.radius+=3
            s.set_speed(s.get_speed()+1)
                
        self.radius=self.radius+self.change        
        self.change=-(self.change)
                
    def display(self,canvas):
       canvas.create_oval(self._x-self.radius      , self._y-self.radius,
                                self._x+self.radius, self._y+self.radius,
                                fill="yellow")   
            
        
        
        