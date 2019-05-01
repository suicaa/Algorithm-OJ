def fib(n):
    a = 1
    b = 1
    arr = [a,b]
    if n == 0 and 1:
        return 1
    for i in range(n):
        arr.append(arr[i] + arr[i + 1])
        if len(arr) == n + 1:
            break
    return arr[n]

n = int(input())
print(fib(n))
