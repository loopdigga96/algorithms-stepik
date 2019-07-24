def add(h, value):
    h.append(value)

    i = len(h) - 1
    parent = (i - 1) // 2

    while i > 0 and h[parent] < h[i]:
        temp = h[i]
        h[i] = h[parent]
        h[parent] = temp

        i = parent
        parent = (i - 1) // 2


def heapify(h, i):
    heap_size = len(h)

    while True:

        left_child = 2 * i + 1
        right_child = 2 * i + 2
        largest_child = i

        if left_child < heap_size and h[left_child] > h[largest_child]:
            largest_child = left_child

        if right_child < heap_size and h[right_child] > h[largest_child]:
            largest_child = right_child

        if largest_child == i:
            break

        temp = h[i]
        h[i] = h[largest_child]
        h[largest_child] = temp
        i = largest_child
    return h


def get_max(h):
    heap_size = len(h)
    result = h[0]
    h[0] = h[heap_size - 1]
    del h[heap_size - 1]
    return result


if __name__ == "__main__":
    n = int(input())
    heap = []

    for _ in range(n):
        data = input().split()

        if data[0] == 'ExtractMax':
            #print(heap)
            print(get_max(heap))
            heapify(heap, 0)
            #print(heap)
            #print('-'*100)
        elif data[0] == 'Insert':
            x = int(data[1])
            add(heap, x)
            #print(heap)
