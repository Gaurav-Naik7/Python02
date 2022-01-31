import Arithmatic

def main():
    no1=int(input("Enter first number: "))
    no2=int(input("Enter second number: "))
    sum=Arithmatic.Add(no1,no2)
    subtraction=Arithmatic.Sub(no1,no2)
    multuplication=Arithmatic.Mult(no1,no2)
    division=Arithmatic.Div(no1,no2)

    print("Addition: ",sum,"Subtraction: ",subtraction,"Multiplication: ",multuplication,"Division: ",division)

if __name__=="__main__":
    main()
