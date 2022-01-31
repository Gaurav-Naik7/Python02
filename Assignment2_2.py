def stars(value):
    for i in range(value):
        print(value*"* ")

def main():
    no=int(input("Enter a number: "))
    stars(no)

if __name__=="__main__":
    main()
