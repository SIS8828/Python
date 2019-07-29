
class Car:
    def ride(self):
        print("Run")

class FlyingCar(Car):
    def ride(self):
        super().ride() # run           # super() 를 통해 부모클래스 매서드 호출.
        print("Fly")

if __name__ == '__main__':
    my_car = FlyingCar()
    my_car.ride() # Fly

