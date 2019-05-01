def len_last_word(s):
    a = str.split(s)
    if s == " ":
        return (len(a))
    else:
        return len(a[-1])
s = input()
print(len_last_word(s))
