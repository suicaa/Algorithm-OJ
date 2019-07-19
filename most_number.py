'''
[3, 3, 3, 2, 2, 1]
'''
def most_number(arr):

    most = 0
    for i in arr:
        count = 0
        for j in arr:
            if i == j:
                count += 1
        if count > most:
            ind = i
            most = count
    return ind


arr = list(input())
print(most_number(arr))

