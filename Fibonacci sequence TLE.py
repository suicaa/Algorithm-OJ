def fib(n):
    a = 1
    b = 1
    arr = [a,b]
    if n == 1 and 2:
        return 1
    for i in range(n + 1):
        arr.append(arr[i] + arr[i + 1])
        if len(arr) == n + 2:
            break
    return arr[n - 1]

n = int(input())
print(fib(n))
