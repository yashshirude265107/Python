# Input from user
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# Check which is greater
if num1 > num2:
    print(f"{num1} is greater than {num2}")
elif num2 > num1:
    print(f"{num2} is greater than {num1}")
else:
    print("Both numbers are equal.")
