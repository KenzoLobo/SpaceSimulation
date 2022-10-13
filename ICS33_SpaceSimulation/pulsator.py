# A Pulsator is a Black_Hole; it updates as a Black_Hole
#   does, but also by growing/shrinking depending on
#   whether or not it eats Prey (and removing itself from
#   the simulation if its dimension becomes 0), and displays
#   as a Black_Hole but with varying dimensions 


from blackhole import Black_Hole


class Pulsator(Black_Hole): 
    max=30
    
    def __init__(self,x,y,width,height):
        Black_Hole.__init__(self,x,y,width,height)
        self.tbm=0
        
    def update(self,model):
        eaten=Black_Hole.update(self,model)
        
        if(len(eaten)>0):
            self.tbm=0
            self.radius+=0.5*len(eaten)
            self.change_dimension(len(eaten),len(eaten))
        else:
            self.tbm+=1
            if self.tbm==30:
                self.radius-=0.5
                self.change_dimension(-1,-1)
                self.tbm=0
                
            if self.radius<=0:
                model.remove(self)
            
        
        return eaten
        
