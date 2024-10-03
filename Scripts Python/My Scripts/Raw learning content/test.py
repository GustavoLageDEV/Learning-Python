# RESOLUÇAO REVISADA
class Line():
    
    def __init__(self,coor1,coor2):

        self.coor1 = coor1
        self.coor2 = coor2
    
    def distance(self):

        x1,y1 = self.coor1
        x2,y2 = self.coor2
        # d = √((x_2-x_1)²+(y_2-y_1)²)  
        return ((x2-x1)**2 + (y2-y1)**2)**0.5
    
    def slope(self):

        x1,y1 = self.coor1
        x2,y2 = self.coor2
        #return m = (y2 - y1)/(x2 - x1)
        return (y2-y1)/(x2-x1)
    

p2 = 25
p1 = Line(3,8)

print("{}".format(p1))