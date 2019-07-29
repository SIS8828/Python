class Car:
    def __init__(self): # 변수선언시 self로 접근해야된다.
        self.color = 0xFF0000 # 차량색상
        self.wheel_size = 16 # 바퀴크기
        self.displacement = 2000 # 배기량

    def forward(self): #전진
        pass

    def backward(self): #후진
        pass

    def turn_left(self): # 좌회전
        pass

    def turn_right(self):  # 우회전
        pass

if __name__ == '__main__':
    my_car = Car() # Car 클래스의 객체 my_car

    print('0x{0:02X}'.format(my_car.color))
    # my_car 멤버변수 접근, 02X -> 2자리의 16진수로  출력하되,
    # 2자리가 안되면 빈자리로 0을채워서 출력

    print(my_car.wheel_size)
    print(my_car.displacement)

    # my_car 멤버메서드 접근
    my_car.forward()
    my_car.backward()
    my_car.turn_left()
    my_car.turn_right()


