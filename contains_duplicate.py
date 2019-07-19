def contains_duplicate(arr):
    a = 0
    for i in arr:
        for j in arr:
            if i == j:
                print("debuger")
                a += 1
    if a >= len(arr):
        print(a)
        return True

    return False


arr = list(input())
print(contains_duplicate(arr))