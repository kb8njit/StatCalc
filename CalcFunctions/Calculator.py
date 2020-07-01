from CalcFunctions.Addition import addition
from CalcFunctions.Subtraction import subtraction
from CalcFunctions.Multiplication import multiplication
from CalcFunctions.Division import division
from CalcFunctions.Square import square
from CalcFunctions.SquareRoot import squareroot

class Calculator:
    result = 0

    def add(self, a, b):
        self.result = addition(a, b)
        return self.result

    def subtract(self, a, b):
        self.result = subtraction(a, b)
        return self.result

    def multiply(self, a, b):
        self.result = multiplication(a, b)
        return self.result

    def divide(self, a, b):
        self.result = division(a, b)
        return self.result

    def square(self, a):
        self.result = square(a)
        return self.result

    def squareroot(self, a):
        self.result = squareroot(a)
        return self.result
