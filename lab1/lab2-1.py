class Calculator:
    def __init__(self, value):
        self.value = value
    
    def __add__(self, other):
        return self.value + other.value

    def __sub__(self, other):
        return self.value - other.value

    def __mul__(self, other):
        return self.value * other.value

    def __truediv__(self, other):
        return self.value / other.value
    
x, y = input("Enter num1 num2 : ").split(",")

x, y = Calculator(int(x)), Calculator(int(y))

print(x+y, x-y, x*y, x/y, sep="\n")
