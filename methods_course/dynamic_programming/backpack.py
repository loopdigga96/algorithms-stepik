"""
Первая строка входа содержит целые числа  W  1≤W≤10^4 и 1≤n≤300 — вместимость рюкзака и число золотых слитков.
Следующая строка содержит nn целых чисел 0≤w_1,…,w_n≤10^5, задающих веса слитков.
Найдите максимальный вес золота, который можно унести в рюкзаке.

Sample input:
10 3
1 4 8
Sample Output:
9

"""


def backpack(capacity, n, weights):
    d = [[0 for j in range(n + 1)] for i in range(capacity + 1)]

    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            d[w][i] = d[w][i - 1]
            c = weights[i - 1]

            if c <= w:
                d[w][i] = max(d[w][i], d[w - c][i - 1] + c)

    return d[-1][-1]


if __name__ == '__main__':
    capacity, n = map(int, input().split())
    weights = list(map(int, input().split()))

    print(backpack(capacity, n, weights))
