"""
Дана число 1≤n≤10^2 ступенек лестницы и целые числа −10^4≤a1,…,an≤10^4,
которыми помечены ступеньки. Найдите максимальную сумму, которую можно получить,
идя по лестнице снизу вверх (от нулевой до n-й ступеньки), каждый раз поднимаясь
на одну или две ступеньки.
Sample Input 1:
2
1 2
Sample Output 1:
3
Sample Input 2:
2
2 -1
Sample Output 2:
1
Sample Input 3:
3
-1 2 1
Sample Output 3:
3
"""


def get_max_num(a, n):
    d = [0, a[0]]
    a = [0] + a

    for i in range(2, n + 1):
        d.append(max(d[i - 1] + a[i], d[i - 2] + a[i]))

    return d[-1]


if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    print(get_max_num(a, n))
