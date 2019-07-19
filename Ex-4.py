def fib(n):
    a = 1
    b = 1
    if n == 0 and 1:
        return 1
    for i in range(n):
        b, a = b + a, b
    return a

n = int(input())
print(fib(n))
