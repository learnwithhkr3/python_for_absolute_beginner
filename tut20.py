# list = ["apple","banana","mango","orange"]

# print(len("talib"))

# def Greet(firstname, lastname):
#     """Greeeting"""
#     print("Good Morning", firstname+" "+lastname)
#     print("Have a nice Day")


# print(Greet("hkr","hasan"))
# Greet("hkr")
# Greet()
# Greet()


# def function1(n1,n2):
#     return n1*n2

# print(function1(40,26))

# print(Greet.__doc__)



def MyLen(data):
    """Retern lentgh any container"""
    count = 0
    for i in data:
        count += 1
    return count

print(MyLen("talib"))


