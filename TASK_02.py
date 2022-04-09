# Solution to Task 2

class Vehicle:

    def __init__(self):
        self.x = 0
        self.y = 0

    def moveUp(self):
        self.y+=1

    def moveDown(self):
        self.y-=1

    def moveRight(self):
        self.x+=1

    def moveLeft(self):
        self.x-=1

    def __str__(self):
        return '('+str(self.x)+' , '+str(self.y)+')'


class Vehicle2010(Vehicle):

    def __init__(self):
        super().__init__()

    def moveLowerLeft(self):
        Vehicle2010.moveDown(self)
        Vehicle2010.moveLeft(self)

    def moveLowerRight(self):
        Vehicle2010.moveDown(self)
        Vehicle2010.moveRight(self)

    def moveUpperLeft(self):
        Vehicle2010.moveUp(self)
        Vehicle2010.moveLeft(self)

    def moveUpperRight(self):
        Vehicle2010.moveUp(self)
        Vehicle2010.moveRight(self)

    def equals(self, target):
        if self.x == target.y:
            return True
        else:
            return False


if __name__ == "__main__":

    print('Part 1')
    print('------')
    car = Vehicle()
    print(car)
    car.moveUp()
    print(car)
    car.moveLeft()
    print(car)
    car.moveDown()
    print(car)
    car.moveRight()
    print(car)
    print('------')
    print('Part 2')
    print('------')
    car1 = Vehicle2010()
    print(car1)
    car1.moveLowerLeft()
    print(car1)
    car2 = Vehicle2010()
    car2.moveLeft()
    print(car1.equals(car2))
    car2.moveDown()
    print(car1.equals(car2))
    print('------')
