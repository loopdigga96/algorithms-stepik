def longest_non_increasing_subsequence(a):
    d = []
    p = []
    for i in a:
        d.append(0)
        p.append(0)

    for i in range(len(a)):
        d[i] = 1
        p[i] = -1

        for j in range(0, i):
            if a[j] >= a[i]:
                if d[j] + 1 > d[i]:
                    d[i] = 1 + d[j]
                    p[i] = j

    ans = d[0]
    pos = 0
    for i, elem in enumerate(d):
        if d[i] > ans:
            ans = d[i]
            pos = i

    seq = []

    while pos != -1:
        seq.append(pos + 1)
        pos = p[pos]

    return ans, reversed(seq)


if __name__ == '__main__':
    # n = int(input())
    # a = list(map(int, input().split()))
    a = [5, 3, 4, 4, 2]
    ans, seq = longest_non_increasing_subsequence(a)
    print(ans)
    print(*seq)

    # TODO: use upper bound
    # TODO: http://e-maxx.ru/algo/longest_increasing_subseq_log
