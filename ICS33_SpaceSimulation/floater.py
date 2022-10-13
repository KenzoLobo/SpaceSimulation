# A Floater is Prey; it updates by moving mostly in
#   a straight line, but with random changes to its
#   angle and speed, and displays as ufo.gif (whose
#   dimensions (width and height) are computed by
#   calling .width()/.height() on the PhotoImage 


#from PIL.ImageTk import PhotoImage
from prey import Prey
import math
import random 


class Floater(Prey): 
    radius=5
    def __init__(self,x,y,width,height):
        self.randomize_angle()
        self.set_speed(5)
        angle=self.get_angle()
        Prey.__init__(self,x,y,width,height,angle,5)
    
    def update(self,model):
        x=random.random()
        if (x>0 and x <0.3): #should be true 30% of the time
            change_speed=random.uniform(-0.5,0.5)
            new_speed=self.get_speed()+change_speed
            
            if(new_speed>7 or new_speed<3):
                new_speed-=(2*change_speed)

            self.set_speed(new_speed)
            
            change_angle=random.uniform(-0.5,0.5)
            new_angle=self.get_angle()+change_angle
            self.set_angle(new_angle)
            
            
        self.move()
        self.wall_bounce()
    
    def display(self,canvas):
        canvas.create_oval(self._x-self.radius      , self._y-self.radius,
                                self._x+self.radius, self._y+self.radius,
                                fill="red")