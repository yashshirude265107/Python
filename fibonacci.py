#Write a function that returns the nth fibonacci number.
def fibo():
    a = 0
    b = 1
    for i in range(1, 8):
      sum1 = a+b
      print (sum1)
      a,b=b,sum1
fibo()    
    
print("--------------------------------")    
#WAP to find maximum among three

def maximum(a,b,c):
    return max(20,50,10)
    

    res = maximum(23,45,2)
    print("Menimum number",res)    