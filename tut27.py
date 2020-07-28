import sys
sys.setrecursionlimit(10)
# print(sys.getrecursionlimit())

count = 1
def Greet():
    global count
    count += 1
    print("hello",count)
    Greet()

Greet()