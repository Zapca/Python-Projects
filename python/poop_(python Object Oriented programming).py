class Car:
    def __init__(self,name=None,model=None,price=None,speed=None):
        self.name=name
        self.model=model
        self.price=price
        self.speed=speed
    
    def start(self):
        print('The car has started!!')

car1=Car()
car1.name='Toyota'
car1.model='cortello'
car1.speed=160
car1.price='$10,000'
print(car1.name,car1.speed,car1.model,car1.price)
# car1.start()

car2=Car('Audi','a4','$125,000',180)
print(car2.name,car2.speed,car2.model,car2.price)
# car2.start()

class Bike(Car):
    def stop(self):
        print('Wtf the car just stopped!!')
    def k(self):
        super().start()
    

car3=Bike()
car3.stop()
car3.start()
