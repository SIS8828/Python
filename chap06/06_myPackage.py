from my_package import calculator
from my_package.package2 import calc

if __name__== '__main__':
    print(calculator.plus(10,5))
    print(calculator.divide(10, 5))
    print(calculator.multiply(10, 5))
    print(calculator.minus(10, 5))
    print(calc.plus(20,5))
    print(calc.divide(20, 5))
    print(calc.multiply(20, 5))
    print(calc.minus(20, 5))

