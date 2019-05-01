def mat_multi(a,b):
    c=[[0,0],[0,0]]
    for i in range(2):
         for j in range(2):
              for k in range(2):
                  c[i][j] += a[i][k]*b[k][j]
    return c

def power(y, m):
    if n == 1:
        return y
    ans = power(mat_multi(y,y),m / 2)
    if n % 2:
        ans = mat_multi(y,ans)
    return ans

def fib(n):
    q = [[1,1],[1,0]]
    if n == 0:
        return 0
    if n == 1:
        return 1
    return power(q, n - 1)[0][0]

n = int(input())
print(fib(n))
