def cummulative_sum(arr):
    if n == 1:
        return [arr[0]]
    list = [arr[0]]
    a = 0
    arr[a] = arr[0]
    while a < n-1:
        if a < n-1:
            list.append(arr[a + 1] + list[-1])
            a += 1
    return list
n = int(input())
arr = []
for i in range(n):
  arr.append(int(input()))
result = cummulative_sum(arr)
print(result)

