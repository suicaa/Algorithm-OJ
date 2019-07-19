'''
实现一个函数 unique_trees(n): 接收一个整数参数 n，n >= 1，返回有 n 个结点、且结构互不相同的二叉树的个数。
注意：
本题仅考虑结构互不相同的二叉树，即连接方式相同、但值不同的二叉树，视为相同的二叉树。
Eg.Given n = 3, there are a total of 5 unique BST's:

   1         3     3      2      1
    \      /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
n = 3   output = 5
'''
def unique_trees(n):
    if n <= 1:
        return 1
    cache = [1, 1]
    for i in range(2, n + 1):
        count = 0
        for j in range(0, i):
            count += cache[j] * cache[i - 1 - j]
        cache.append(count)
    return cache[-1]

n = int(input())
print(unique_trees(n))
