'''
def single_number(arr):
    list = []
    for i in range(len(arr)):
        for j in range(len(arr)):
            if i == j:
                continue
            if arr[i] == arr[j]:
                 list.append(arr[i])
    lst = [i for i in arr if i not in list]
    return lst[-1]

arr = list(input())
print(single_number(arr))
Time Limited Error
'''

def single_number(arr):
    XOR_operator = 0
    for i in arr:
        XOR_operator ^= i
    return XOR_operator
arr = list(input())

print(single_number(arr))
