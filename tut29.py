

# def func(n):
#     return n*n

# func1 = lambda x,n: x+n #anomynous

# print(func(5))
# print(func1(10,25))

def function1(n):
    return lambda x: x*n

double = function1(2)
triple = function1(3)

print(double(2))
print(triple(2))
