# Solution to Task 6

class Shape:

    def __init__(self, name='Default', height=0, base=0):
        self.area = 0
        self.name = name
        self.height = height
        self.base = base

    def get_height_base(self):
        return "Height: "+str(self.height)+", Base: "+str(self.base)



class Triangle(Shape):

    def __init__(self, name="default", height=0, base=0):
        super().__init__(name, height, base)

    def calcArea(self):
        self.area = 0.5 * (self.height*self.base)
        return self.area

    def printDetail(self):
        return f'{self.get_height_base()}\nArea: {self.calcArea()}'


class Trapezoid(Shape):

    def __init__(self, name="default", height=0, base=0, side=0):
        super().__init__(name, height, base)
        self.side = side

    def calcArea(self):
        self.area = 0.5 * (self.height*(self.base+self.side))
        return self.area

    def printDetail(self):
        return f'{self.get_height_base()}, Side_A = {self.side}\nArea: {self.calcArea()}'


if __name__ == "__main__":

    tri_default = Triangle()
    tri_default.calcArea()
    print(tri_default.printDetail())
    print('--------------------------')
    tri = Triangle('Triangle', 10, 5)
    tri.calcArea()
    print(tri.printDetail())
    print('---------------------------')
    trap = Trapezoid('Trapezoid', 10, 6, 4)
    trap.calcArea()
    print(trap.printDetail())
