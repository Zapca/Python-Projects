class Car:
    def __init__(self,name=None,model=None):
        self.name=name
        self.model=model
    
    def start(self):
        print('The Car has started!!')

car1=Car('toyota','A3')
car1.name='Audi'
print(car1.name,car1.model)
car1.start()

class Engine(Car):
    def i(self):
        print('Brummm Brumm')
    def j(self):
        super().start()

car2=Engine()
car2.i()
car2.j()