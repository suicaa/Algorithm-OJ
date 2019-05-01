def best_transactions(arr):
    return (arr.index(min(arr)) , arr.index(max(arr)))

n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))

print(best_transactions(arr))
