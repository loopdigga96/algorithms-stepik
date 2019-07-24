from math import sqrt
if __name__ == "__main__":
    n = int(input())
    kd = (-1.0 + sqrt(1.0 + 8.0 * n)) / 2.0
    k = int(kd)
    print(k)

    s = [i for i in range(1, k)]

    s.append(n - sum(s))
    print(*s)