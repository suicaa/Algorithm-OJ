def reverse(n):
    return ((n%100)%10)*100 + n%100 - ((n%100)%10) + int(n//100)

n = int(input())
print(reverse(n))
