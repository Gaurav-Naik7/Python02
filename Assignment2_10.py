
def pattern(value):
    sum=0
    for i in range(len(value)):
        sum=sum+int(value[i])
    return sum

def main():
    no=input("Enter a number: ")
    ret=pattern(no)
    print(ret)

if __name__=="__main__":
    main()
