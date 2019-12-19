def get_result(size, n):
    queue = []
    current_iter = 0
    result = []

    for i in range(n):
        arrival, duration = input().split()
        arrival = int(arrival)
        duration = int(duration)

        # get last_item
        if i > 0:
            last_item = queue[-1]
        else:
            last_item = (arrival, duration)

        # if we on next time step
        if last_item[0] < arrival:
            current_iter = arrival

            while (current_iter - last_item[0] - last_item[1] <= 0 or last_item[1] == 0) and len(queue) > 0:
                last_item = queue.pop()

        # check before if it is next stop from previous
        if len(queue) == size:
            result.append(-1)
        else:
            if len(queue) == 0:
                result.append(arrival)
            queue.append((arrival, duration))
    return result


if __name__ == '__main__':
    """
    2 8
    0 0
    0 0
    0 0
    1 0
    1 0
    1 1
    1 2
    1 3
    """
    size, n = list(map(int, input().split()))
    result = get_result(size, n)
    print(*result, sep='\n')
