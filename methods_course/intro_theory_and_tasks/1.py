def fib(n):
    result = []
    for i in range(n+1):
        
        if i == 0:
            result.append(0)
        elif i == 1:
            result.append(1)
        else:
            result.append(result[-1]+result[-2])
    return result[-1]

def main():
    n = int(input())
    print(fib(n))


if __name__ == "__main__":
    main()