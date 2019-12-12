"""
У вас есть примитивный калькулятор, который умеет выполнять всего три операции с
текущим числом x: заменить на 2x, 3x или x+1. По данному целому числу 1≤n≤10^5 определите минимальное число операций k,
необходимое, чтобы получить n из 1. Выведите k и последовательность промежуточных чисел.

Sample Input 1:
1
Sample Output 1:
0
1

Sample Input 2:
5
Sample Output 5:
3
1 2 4 5

Sample Input 3:
96234
Sample Output 1:
14
1 3 9 10 11 22 66 198 594 1782 5346 16038 16039 32078 96234
"""


def get_best_choice(i, d):
    candidates = []
    if i > 0:
        candidates.append(1 + d[i - 1])
    if i // 2 > 0 and i % 2 == 0:
        candidates.append(1 + d[i // 2])
    if i // 3 > 0 and i % 3 == 0:
        candidates.append(1 + d[i // 3])

    return min(candidates)


def get_k(x):
    d = [0 for i in range(x + 1)]

    for i in range(2, x + 1):
        d[i] = get_best_choice(i, d)

    seq = get_sequence(d, x)
    return d[-1], seq


def get_sequence(d, x):
    best = d[-1]
    i = x
    seq = [x]

    while i > 0:
        d_i = d[i]

        if d_i < best:
            if (seq[-1] - 1) == i or (seq[-1] / 2) == i or (seq[-1] / 3) == i:
                best = d_i
                seq.append(i)
        i -= 1
    return list(reversed(seq))


if __name__ == '__main__':
    x = int(input())
    ans, seq = get_k(x)

    print(ans)
    print(*seq)
