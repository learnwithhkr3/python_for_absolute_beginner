# *args
# *kwargs


# def addition(n1, n2):
#     return n1 + n2


# def addition(*args):
#     # print(type(args))
#     sum = 0
#     for item in args:
#         sum = sum + item
#     return sum


# print(addition(65, 52, 85))

# {"firstname": "hkr", "lastname": "hasan", "age": 22}


# Firstname is Sita
# Lastname is Sharma
# Age is 22
# Phone is 1234567890


def print_function(*args, **kwargs):
    print(args[0])
    for key, value in kwargs.items():
        print(f"{key} is {value}")


print_function("ajay", firstname="hkr", lastname="hasan")
