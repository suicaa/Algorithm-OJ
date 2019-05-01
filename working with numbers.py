from math import *
print(2 + 4.35)
print(10%3)
my_num = 5
print(str(my_num) + " is my favorite number")
my_num2 = -3
print(abs(my_num2))
print(pow(3,2))
print(max(4,18))
print(round(3.8))
print(sqrt(81))

x = 10
while x > 0:
    print(2*x)
    x = x-1
def f(x):
    if x < 0:
        return abs(x)
    elif 0 <= x < 2:
        return sqrt(x + 1)
    elif 2 <= x < 4:
        return pow(x + 2, 5)
    return 2 * x + 5
x = float(input())

print('%.2f'%f(x))