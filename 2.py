class Vehicle:
    def printConsumation(self):
        print('none')

class MotorVehicle(Vehicle):
    def printConsumation(self):
        print('medium')

class Car(MotorVehicle):
    pass

car= Car()
car.printConsumation()