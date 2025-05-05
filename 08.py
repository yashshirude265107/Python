# generate 0 1 1 2 3 5 8... fibonacci series

a = 0
b = 1
print(a)
print(b)
for i in range(10):
    c=a+b
    print(c)
    a=b
    b=c 