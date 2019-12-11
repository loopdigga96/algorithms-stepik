"""
В первой строке задано два целых числа 1≤n≤50000 и 1≤m≤50000 1  — количество отрезков и точек на прямой, соответственно.
Следующие n строк содержат по два целых числа  (ai≤bi ​) — координаты концов отрезков.
Последняя строка содержит m m m целых чисел — координаты точек. Все координаты не превышают 10^8  по модулю.
Точка считается принадлежащей отрезку, если она находится внутри него или на границе.
Для каждой точки в порядке появления во вводе выведите, скольким отрезкам она принадлежит.
"""


def swap(a, b):
    c = a
    a = b
    b = c
    return a, b


def partition(a, l, r, cmp_func):
    x = a[l]
    j = l

    for i in range(l + 1, r + 1):
        if cmp_func(a[i], x):
            j += 1
            a[j], a[i] = swap(a[j], a[i])
    a[l], a[j] = swap(a[l], a[j])
    return j


def qsort(a, l, r, cmp_fun):
    if l >= r:
        return
    m = partition(a, l, r, cmp_fun)
    qsort(a, l, m - 1, cmp_fun)
    qsort(a, m + 1, r, cmp_fun)


if __name__ == "__main__":
    from copy import deepcopy
    import bisect

    n, m = input().split()
    a = []

    for _ in range(int(n)):
        st, en = tuple(map(int, input().split()))
        a.append((st, en))

    points = list(map(int, input().split()))

    b = deepcopy(a)
    starts = sorted((row[0] for row in a))
    ends = sorted((row[1] for row in b))

    for p in points:
        st = bisect.bisect_right(starts, p)
        en = bisect.bisect_left(ends, p)
        print(st - en, end=' ')
