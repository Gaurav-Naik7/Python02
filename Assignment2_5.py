def prime(value):
    for i in range(2,value):
        if value%i==0:
            print("It is not a Prime number")
            break
    else:
        print("It is a prime number")


def main():
    no=int(input("Enter a number: "))
    prime(no)

if __name__=="__main__":
    main()
