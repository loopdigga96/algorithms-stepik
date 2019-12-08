"""
В первой строке даны целое число 1≤n≤10^5 и массив A[1…n]из n различных натуральных чисел, не превышающих 10^9,
в порядке возрастания, во второй — целое число 1≤k≤10^5 k натуральных чисел b1,…,bk​, не превышающих 10^9.
Для каждого i от 1 до k необходимо вывести индекс 1≤j≤n, для которого A[j]=b_i​, или −1, если такого j нет.
"""


def search(a, value):
    l = 0
    r = len(a) - 1

    while l <= r:
        m = (l + r) // 2
        tmp = a[m]

        if tmp == value:
            return m + 1
        elif tmp > value:
            r = m - 1
        else:
            l = m + 1
    return -1


if __name__ == "__main__":
    a = tuple(map(int, input().split(' ')[1:]))
    b = tuple(map(int, input().split(' ')[1:]))
    for k in b:
        print(search(a, k), end=' ')
