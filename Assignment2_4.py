def addf(value):
    sum=0
    for i in range(1,value):
        if value%i==0:
            sum=sum+i
    return sum


def main():
    no=int(input("Enter a number: "))
    ret=addf(no)
    print(ret)

if __name__=="__main__":
    main()
