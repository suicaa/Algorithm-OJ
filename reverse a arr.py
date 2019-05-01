def arr_reverse(arr):
    reverse = []
    while len(arr) > 0:
        reverse.append(arr[-1])
        del arr[-1]
    return reverse


n = int(input())
arr = []
for i in range(n):
  arr.append(int(input()))
print(arr_reverse(arr))
