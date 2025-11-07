#LARGEST AMONG 3 NUMBERS
a=int(input("enter the first num\n"))
b=int(input("enter the second num\n"))
c=int(input("enter the third num\n"))
if (a==b and b==c):
    print("three num are equal")
elif (a>b and a>c):
    print(a,"is larger")
elif (b>a and b>c):
    print(b,"is larger")
else:
    print(c,"is larger")       
