#FIBONACCI SERIES
num=int(input("enter the number of n terms\n"))
i=3
a=0
b=1
print("the fibonacci series of",num," terms=",a,b,end=" ")
while (i<=num):
    c=a+b
    print(c,end=" ")
    a=b
    b=c
    i=i+1
