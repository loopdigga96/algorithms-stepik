def swap(a, b):
    c = a; a = b; b = c
    return a, b


def partition(a, l, r, cmp_func):
    x = a[l]
    j = l

    for i in range(l+1, r+1):
        if cmp_func(a[i], x):
            j += 1
            a[j], a[i] = swap(a[j], a[i])
    a[l], a[j] = swap(a[l], a[j])
    return j


def qsort(a, l, r, cmp_fun):
    if l >= r:
        return
    m = partition(a, l, r, cmp_fun)
    qsort(a, l, m-1, cmp_fun)
    qsort(a, m+1, r, cmp_fun)


if __name__ == "__main__":
    from copy import deepcopy
    from functools import cmp_to_key
    # n, m = input().split()
    a = []

    # lines = [[0, 5],
    #          [7, 10]]
    # points = [1, 6, 11]
    lines = [[0, 3],
             [1, 3],
             [2, 3],
             [3, 4],
             [3, 5],
             [3, 6]]
    points = [1, 2, 3, 4, 5, 6]

    LEFT = -1
    POINT = 0
    RIGHT = 1
    for st, en in lines:
    # for _ in range(int(n)):
    #     st, en = tuple(map(int, input().split()))
        a.extend(((st, LEFT, -1), (en, RIGHT, -1)))
    #     a.append((st, en))

    # points = list(map(int, input().split()))
    for idx, p in enumerate(points):
    #      a.append((p, 'point'))
        a.append((p, POINT, idx))

    def sort_logic(a, b):
        if a[0] != b[0]:
            return a[0] < b[0]
        else:
            return a[1] < b[1]

    qsort(a, 0, len(a) - 1, lambda a, b: sort_logic(a, b))
    print(a)
    print(points)

    cur = 0
    answer = list(range(len(points)))
    for obj in a:
        if obj[1] == LEFT:
            cur += 1
        elif obj[1] == RIGHT:
            cur -= 1
        elif obj[1] == POINT:
            idx = obj[2]
            answer[idx] = cur
        else:
            pass


    print(*answer)
    # https://www.youtube.com/watch?v=jvRWnf4q9C8
