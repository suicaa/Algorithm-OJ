def arr_min(arr):
    return min(arr)

n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))
result = arr_min(arr)
print(result)
