def longest_increasing_subsequence(a):
    d = [0 for i in a]

    for i in range(len(a)):
        d[i] = 1

        for j in range(0, i):
            # if a[j] < a[i]:
            if a[i] % a[j] == 0:
                d[i] = max(d[i], d[j] + 1)

    return max(d)


if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    print(longest_increasing_subsequence(a))
