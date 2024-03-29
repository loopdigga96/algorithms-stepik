"""
Первая строка содержит число 1≤n≤105, вторая — массив A[1…n], содержащий натуральные числа, не превосходящие 10^9
Необходимо посчитать число пар индексов 1≤i<j≤n, для которых A[i]>A[j]. (Такая пара элементов называется инверсией массива.
Количество инверсий в массиве является в некотором смысле его мерой неупорядоченности: например,
в упорядоченном по неубыванию массиве инверсий нет вообще, а в массиве, упорядоченном по убыванию, инверсию образуют каждые два элемента.)
"""


def merge(a, b, inversions):
    result = []
    len_a = len(a)
    len_b = len(b)
    i = 0
    j = 0

    while i < len_a and j < len_b:
        if a[i] > b[j]:
            result.append(b[j])
            inversions += len_a - i
            j += 1
        else:
            result.append(a[i])
            i += 1

    if len(a[i:]):
        result.extend(tuple(a[i:]))
    elif len(b[j:]):
        result.extend(tuple(b[j:]))

    return result, inversions


def merge_sort(a):
    if len(a) > 1:
        m = len(a) // 2
        res1, inversion1 = merge_sort(a[:m])
        res2, inversion2 = merge_sort(a[m:])
        return merge(res1, res2, inversion1 + inversion2)
    else:
        return [a], 0


if __name__ == "__main__":
    import sys

    n = int(sys.stdin.readline())
    a = [int(_) for _ in sys.stdin.readline().split()]
    arr, inv = merge_sort(a)
    print(inv)
