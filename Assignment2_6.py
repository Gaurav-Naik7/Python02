def pattern(value):
    while (value>0):
        print(value*"* ",end="\n")
        value=value-1

def main():
    no=int(input("Enter a number: "))
    pattern(no)

if __name__=="__main__":
    main()

'''
def pattern(value):
    while (value>0):
        print(value*"* ")
        value=value-1

def main():
    no=int(input("Enter a number: "))
    pattern(no)

if __name__=="__main__":
    main()
'''
