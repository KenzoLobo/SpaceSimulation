# A Hunter class is derived from a Pulsator and then Mobile_Simulton base.
#   It inherits updating+displaying from Pusator/Mobile_Simulton: it pursues
#   any close prey, or moves in a straight line (see Mobile_Simultion).


from prey  import Prey
from pulsator import Pulsator
from mobilesimulton import Mobile_Simulton
from math import atan2


class Hunter(Pulsator, Mobile_Simulton):
    vision=200  
    def __init__(self,x,y,width,height):
        Pulsator.__init__(self,x,y,width,height)
        self.randomize_angle()
        self.set_speed(5)
        
    
    def update(self,model):
        def in_range(xy):
            dist=self.distance(xy)
            if dist<self.vision:
                return True 
            else:
                return False
        close_by=model.find(in_range)
        
        if len(close_by)>0: 
            close_by=sorted(close_by,key=lambda s: self.distance(s.get_location()))
            closest=close_by[0]
            y_diff=closest.get_location()[1]-self.get_location()[1]
            x_diff=closest.get_location()[0]-self.get_location()[0]
            new_angle=atan2(y_diff,x_diff)
            self.set_angle(new_angle)
            
        
                
        Pulsator.update(self,model)
        self.move()
        self.wall_bounce()
