"""

 Задача на программирование повышенной сложности: наибольшая невозрастающая подпоследовательность


 Дано целое число 1≤n≤10^5 и массив A[1…n], содержащий неотрицательные целые числа, не превосходящие 10^9.
 Найдите наибольшую невозрастающую подпоследовательность в A.
 В первой строке выведите её длину k, во второй — её индексы 1≤i[1]<i[2]<…<i[k]≤n
 (таким образом, A[ i[1] ]≥A[ i[2] ]≥…≥A[ i[n] ]).

 Sample Input:
 5
 5 3 4 4 2

 Sample Output:
 4
 1 3 4 5

"""
from bisect import bisect_right

if __name__ == '__main__':

    _, a, d, prev = input(), list(map(int, input().split())), [], []
    for i, x in enumerate(a):
        j = bisect_right(d, [-x, i])
        if j == len(d):
            d.append([-x, i])
        else:
            if -d[j][0] < x:
                d[j] = [-x, i]

        prev.append(d[j - 1][1] if j else None)

    out = [d[-1][1]]
    while prev[out[-1]] is not None:
        out.append(prev[out[-1]])

    print(len(out), ' '.join(str(x + 1) for x in reversed(out)), sep='\n')
