'''
def pattern(value):
    for i in range(1,(value+1)):
        j=0
        while j<i:
            print(i,end=" ")
            j=j+1
        print("\n")
'''

def pattern(value):
    for i in range(1,(value+1)):
        for j in range(1,(value+1)):
            if i>=j:
                print(j,end=" ")
        print("\n")

def main():
    no=int(input("Enter a number: "))
    pattern(no)

if __name__=="__main__":
    main()
