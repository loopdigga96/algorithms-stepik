def fib(n):
    result = []
    for i in range(n+1):
        if i == 0:
            result.append(0)
        elif i == 1:
            result.append(1)
        else:
            result = [result[-1], result[-1]+result[-2]]
    return result[-1]

def fib_mod(n, m):
    return fib(n) % m

def find_pisano(n, m):
    pisano = []
    pisano.append(0)
 
    # при делении на 1 остаток будет всегда 0
    if m == 1:
        return pisano
 
    pisano.append(1)
 
    # при m > 0 остатки от деления первого и второго числа Фибоначчи
    # всегда 0 и 1
    if n <= 1:
        return pisano
 
    n0 = 0
    n1 = 1
    for __ in range(m * 6):
        # для ускорения вычисляем полностью числа Фибоначчи
        # берём только остатки по модулю m
        n0, n1 = n1, (n0 + n1) % m
 
        pisano.append(n1 % m)
 
        # Проверяем не начался ли новый период 
        # период всегда начинается с 0 и 1
        if pisano[len(pisano) - 1] == 1 \
            and pisano[len(pisano) - 2] == 0:
            break
    #pisano = pisano
    pisano = pisano[:-2]
    
    return pisano[n % len(pisano)]

def main():
    n, m = map(int, input().split())
    print(find_pisano(n, m))


if __name__ == "__main__":
    main()