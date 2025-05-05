#A decorator in python is a function that modifies the behavior of 
#another function without changing its actual code

# its often used for logging , access contro, timing etc\
    
def decorator_function(original_function):
    def wrapper_function():
        print("Welcome to axis bank!!!")
        original_function()
        print("Thank you for using our services!!!!")
    return wrapper_function    
@decorator_function
def say_hello():
    print("Hello!!!")
    
say_hello()    