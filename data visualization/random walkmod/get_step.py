from random import choice

#class that generates random walks
class RandomWalk():

    #initializing the class attributes
    def __init__(self,num_points=50000):
        self.num_points=num_points
        #All walks start at (0,0)
        self.x_values=[0]
        self.y_values=[0]
     
    
    def fill_walk(self):
        #calculate steps in the walk
        
        #keep walking until we reach the end of walk points
        while len(self.x_values)<self.num_points:
            # Reject moves that go nowhere.
            x_step=get_step()
            y_step=get_step()
           
            if x_step == 0 and y_step == 0:
                continue
            
            # Calculate the next x and y values.
            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step
            #Append steps to steps list x and y values 
            self.x_values.append(next_x)
            self.y_values.append(next_y)

def get_step():
    # Decide which direction to go and how far to go in that direction.
    direction = choice([1, -1])
    distance = choice([0, 1, 2, 3, 4])
    step = direction * distance
    return step   
            
    
        