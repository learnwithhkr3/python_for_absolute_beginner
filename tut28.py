# Factorial
# n! = n * (n-1)

# example:-
#     5! = 5*4*3*2*1 = 120
#     4! = 4*3*2*1 = 24
#     3! = 3*2*1 = 6



def factorial(x):
    if x == 0 or x ==1:
        return 1
    return x * factorial(x-1)

n = int(input("Enter a Number:- "))
print(factorial(n))

factorial(3)          # 1st call with 3
3 * factorial(2)      # 2nd call with 2
3 * 2 * factorial(1)  # 3rd call with 1
3 * 2 * 1             # return from 3rd call as number=1
3 * 2                 # return from 2nd call
6                     # return from 1st call