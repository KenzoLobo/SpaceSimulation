# A Ball is Prey; it updates by moving in a straight
#   line and displays as blue circle with a radius
#   of 5 (width/height 10). 


from prey import Prey


class Ball(Prey): 
    radius=5
    def __init__(self,x,y,width,height):
        self.randomize_angle()
        self.set_speed(5)
        angle=self.get_angle()
        Prey.__init__(self,x,y,width,height,angle,5)
    
    def update(self,model):
        self.move()
        self.wall_bounce()
    
    def display(self,canvas):
       canvas.create_oval(self._x-self.radius      , self._y-self.radius,
                                self._x+self.radius, self._y+self.radius,
                                fill="blue")