def mat_multi(a,b):
    c=[[0,0],[0,0]]
    for i in range(2):
         for j in range(2):
              for k in range(2):
                  c[i][j] += a[i][k]*b[k][j]
    return c

def power(y, m):
    if m == 1:
        return y
    z = y
    y = mat_multi(y,y)
    h = 1
    while h < m/2:
        y = mat_multi(y,y)
    if m % 2:
        odd_result = mat_multi(z,y)
    return odd_result

