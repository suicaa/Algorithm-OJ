def second_smallest(arr):
    a = 0
    while a < n:
        if arr[a + 1] - arr[a] > 0:
            break
        else:
            a += 1
    return arr[a + 1]

n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))
print(second_smallest(arr))
