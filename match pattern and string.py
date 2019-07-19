'''
实现一个函数match，它接收两个参数string和pattern，返回pattern是否匹配string。
string由小写字母组成。
pattern表示一类字符串，定义如下：
字符 a-z 属于pattern，且可以匹配对应单个字母组成的字符串。
字符 a-z 与+拼接的结果属于pattern，且可以匹配该字母出现任意多次（多于一次）的字符串。
例如g+可以匹配ggggg，g。
如果a属于pattern，b是pattern，则ab（a和b的字符串拼接）属于pattern，
且可以匹配的字符串是a匹配的所有字符串和b匹配的所有字符串的两两拼接。
例如 patterna可以匹配的字符串集合是{"a"}，b是{"b"}.ab可以匹配的字符串集合是{"ab"}
例如 patterna+可以匹配的字符串集合是{"a", "aa", "aaa", ...}，b是 {"b"}，
a+b可以匹配的字符串集合是{"ab", "aab", "aaab", "aaaab", ...}
'''
def match(string, pattern):
    if len(string) == 0:
        return False
    si = 0
    for pi, pchar in enumerate(pattern):

        if pchar == "+":
            continue
        elif pi + 1 <= len(pattern) - 1 and pattern[pi + 1] == "+":
            matched = False
            while True:
                if si >= len(string):
                    break
                elif string[si] == pchar:
                    matched = True
                    si += 1
                else:
                    break
            if not matched:
                return  False
        else:
            if si >= len(string) or string[si] != pchar:

                return False
            else:
                si += 1

    return si == len(string)

s = input()
p = input()
print(match(s, p))
