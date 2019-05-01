def takefirst(elem):
    return elem[0]
new_arr = []

def merge_intervals(arr):
    arr.sort(key=takefirst)
    i = 1
    while i < n:
        j = i - 1
        if arr[i - 1][1] > arr[i][0] or arr[i - 1][1] == arr[i][0]:
            while arr[i - 1][1] > arr[i][0] or arr[i - 1][1] == arr[i][0]:
                if i < n:
                    i += 1
                if i < n:
                    continue
                else:
                    break
            new_arr.append([arr[j][0], arr[i - 1][1]])
        else:
            new_arr.append([arr[i][0], arr[i][1]])
            i += 1
    print(i)
    print(j)
    return new_arr

n = int(input())
arr = []
for i in range(n):
  a, b = input().split()
  a, b = int(a), int(b)
  arr.append((a, b))

print(merge_intervals(arr))
