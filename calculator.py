from add import Addition
from sub import Subtraction
from mul import Multiplication
from div import Division


class Calculator:

    def addition(self, n1, n2):
        add = Addition()
        return add.addition(n1, n2)

    def subtraction(self, n1, n2):
        sub = Subtraction()
        return sub.subtraction(n1, n2)

    def multiplication(self, n1, n2):
        mul = Multiplication()
        return mul.multiplication(n1, n2)

    def division(self, n1, n2):
        div = Division()
        return div.division(n1, n2)
