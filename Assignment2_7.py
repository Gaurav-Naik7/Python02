def pattern(value):
    for i in range(1,(value+1)):
        for i in range(1,value+1):
            print(i,end=" ")
        print("\n")


def main():
    no=int(input("Enter a number: "))
    pattern(no)

if __name__=="__main__":
    main()
