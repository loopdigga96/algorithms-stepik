def search(a, value):
    l = 0
    r = len(a)-1

    while l <= r:
        m = (l+r)//2
        tmp = a[m]

        if tmp == value:
            return m+1
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
