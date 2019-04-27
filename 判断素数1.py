num = int(input())
if num > 1:
    for a in range(2, num):
        if (num % a) == 0:
            print("false")
            print(a, "times", num//a, "is", num)
            break
    else:
        print("True")
else:
    print("True")
