
#Q.3)WAP to get average of three numbers

a = int(input("Enter the first number"))
b = int(input("Enter the second number:"))
c = int(input("Enter the third number:"))

if(a > b and a > c):
    print("a is greatest number")
elif(b > a and b > c):
    print("b is gretest number")
else:
    print("c is gretest number")        