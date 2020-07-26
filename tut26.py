# x = 10 #Global
# a = 12 #Global

# def func():
#     # x = 15 #local
#     y = 23 #local 
#     global x
#     x = x * 2 
#     print('inside function:- ',x)

# func()
# # print(x)


def outer():
    x = 25 #local
    def inner():
        global x
        x = 10
    print('before calling inner()',x)
    inner()
    print('after calling inner()',x)


outer()
print(x)