"""
Первая строка содержит число 1≤n≤10^4, вторая — n n n натуральных чисел, не превышающих 10.
Выведите упорядоченную по неубыванию последовательность этих чисел.
"""


def count_sort(a):
    b = [0 for i in range(11)]

    for element in a:
        b[element] += 1

    for j in range(1, len(b)):
        b[j] += b[j - 1]

    a_sorted = [0 for i in range(len(a))]

    for j in range(len(a) - 1, -1, -1):
        val = a[j]
        index = b[val] - 1
        a_sorted[index] = val
        b[a[j]] -= 1
    return a_sorted


if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))

    print(*count_sort(a))
