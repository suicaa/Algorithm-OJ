def exp(epsilon, x):
    e = 0
    cur = 1
    n = 1
    while cur >= epsilon:
        e += cur
        cur = cur * x / n
        n += 1
    e += cur
    return e

epsilon = float(input())
x = float(input())
result = exp(epsilon, x)
print("%.6f" % result)
