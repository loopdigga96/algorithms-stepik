"""
Дано целое число 10^31≤n≤10^3 и массив A[1…n] натуральных чисел, не превосходящих 2*10^9.
Выведите максимальное 1≤k≤n, для которого найдётся подпоследовательность 1≤i1<i2<…<ik≤n длины kk,
в которой каждый элемент делится на предыдущий (формально: для  всех 1≤j<k, A[i_j] | A[i_{j+1}]).
"""


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
