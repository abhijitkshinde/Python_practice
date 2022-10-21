class Point():

    def __init__(self,x,y):
        self.x = x
        self.y = y


    def getx(self):
        return self.x
point1 = Point(4,8)

print(point1.getx(),'\n',point1.y)