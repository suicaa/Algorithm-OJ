num = int(input())
if num == 3:
    print("True")
if num == 2:
    print("True")
if num == 1:
    print("False")
else:
    i = 2
    while i * i <= num:
        if num % i == 0:
            print("False")
            break
        i += 1
        print("True")
        break
