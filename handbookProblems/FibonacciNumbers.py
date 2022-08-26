n1=0
n2=1
count=0

num=int(input("Enter a number "))
if num<=0:
    print("Please enter a positive number")
elif num==1:
    print(n1)
else:
    print("The fabonacci sequence of the number is:")

    while count<=num:
        print(n1)
        n=n1+n2
        n1=n2
        n2=n
        count=count+1