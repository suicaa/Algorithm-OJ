def k_th_smallest(arr, k):
    arr.sort(reverse=False)
    return arr[k - 1]



arr = input().split(" ")
arr = [int(x) for x in arr]

k = int(input())
print(k_th_smallest(arr, k))
