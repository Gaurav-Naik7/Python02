def Factorial(value):
    mult=1
    for i in range(1,value+1):
        mult=mult*i
    return mult

def main():
    no=int(input("Enter a number: "))
    ret=Factorial(no)
    print(ret)

if __name__=="__main__":
    main()
