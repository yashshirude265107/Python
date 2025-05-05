# WAP to check whether number is even or odd

def evenOdd(x):
    if(x%2==0):
        print("The number passed to the function is even")
    else:
        print("The number is odd")
        
num = int(input("Enter a number to check even or odd"))
evenOdd(num)            