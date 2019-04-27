def two_sum(arr, a):
    n = len(arr)
    for i in range(n + 1):
        if a - arr[i] in arr:
            if arr.index(arr[i]) != arr.index(a - arr[i]):
                return (arr.index(arr[i]) , arr.index(a - arr[i]))
            else:
                return None
        i += 1

print(two_sum([2,2],4))

