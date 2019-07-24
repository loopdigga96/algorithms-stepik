#def fib_digit(n):
#    ...

def fib_digit(n):
    result = []
    for i in range(n+1):
        #print('iter',i)
        if i == 0:
            result.append(0)
        elif i == 1:
            result.append(1)
        else:
            result = [result[-1], (result[-1]+result[-2])%10]
                    #result.append((result[-1]+result[-2])%10)
                    #print(result)

    return result[-1]

def main():
    n = int(input())
    print(fib_digit(n))


if __name__ == "__main__":
    main()