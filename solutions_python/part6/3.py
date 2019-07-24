def swap(a, b):
    c = a; a = b; b = c
    return a, b


def compare(a, b):
    if a <= b:
        return True
    else:
        return False


def partition(a, l, r):
    x = a[l]
    j = l

    for i in range(l+1, r+1):
        if compare(a[i], x):
            j += 1
            a[j], a[i] = swap(a[j], a[i])
    a[l], a[j] = swap(a[l], a[j])
    return j


def qsort(a, l, r):
    if l < r:
        m = partition(a, l, r)
        qsort(a, l, m-1)
        l = m + 1
        # qsort(a, m+1, r)


if __name__ == "__main__":
    import random
    # n, m = input().split()
    a = []
    lines = [[0, 5], [7, 10]]
    points = [1, 6, 11]
    # points = [random.randrange(0, 10**3) for _ in range(10**4)]
    # for _ in range(int(n)):
    for st, en in lines:
        # st, en = tuple(map(int, input().split()))
        a.extend(((st, 'start'), (en, 'end')))

    for p in points:
        a.append((p, 'point'))
    print(a)



    #a = [9, 4, 5, 2, 6, -1, 100, 0, 0, 0]
    #a = [0,1,2,3,4,5,6,7,8,9]
    qsort(a, 0, len(a) - 1)
    a[0], a[1] = swap(a[0], a[1])
    print(a)
