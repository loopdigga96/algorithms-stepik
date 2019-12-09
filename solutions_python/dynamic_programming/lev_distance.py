def diff(c1, c2):
    if c1 != c2:
        return 1
    else:
        return 0


def lev_distance(a, b):
    n = len(a) + 1
    m = len(b) + 1
    d = [[0] * m for i in range(n)]

    for i in range(n):
        d[i][0] = i

    for j in range(m):
        d[0][j] = j

    for i in range(1, n):
        for j in range(1, m):
            cost = diff(a[i - 1], b[j - 1])
            d[i][j] = min(d[i - 1][j] + 1, d[i][j - 1] + 1, d[i - 1][j - 1] + cost)

    return d[n - 1][m - 1]


if __name__ == '__main__':
    a = input()
    b = input()
    print(lev_distance(a, b))
