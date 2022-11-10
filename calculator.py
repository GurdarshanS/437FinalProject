
class Calculator:
    
    def addition(n1, n2):
        return n1+n2

    def subtraction(n1, n2):
        return n1-n2

    def multiplication(n1, n2):
        return n1*n2

    def division(n1, n2):
        return n1/n2


if __name__ == "__main__":
    v1 = int(input("Enter your value 1: "))
    v2 = int(input("Enter your value 2: "))
    op = input("Enter your operator (a,s,m,d): ")
    calc = Calculator
    
    if(op=="a"):
        print(calc.addition(v1,v2))
    elif(op=="s"):
        print(calc.subtraction(v1,v2))
    elif(op=="m"):
        print(calc.multiplication(v1,v2))
    else:
        print(calc.division(v1,v2))