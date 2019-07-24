def sift_up(h):
    h_len = len(h)
    child_id = h_len

    while True:
        parent_id = round((child_id) / 2)

        if 0 < parent_id < h_len:
            parent_value = h[parent_id-1]
            child_value = h[child_id-1]

            if child_value > parent_value:
                h[parent_id-1] = child_value
                h[child_id-1] = parent_value
                child_id = parent_id
            else:
                break
        else:
            break
    return h


def sift_down(h):
    h[0] = h[-1]
    del h[-1]

    parent_id = 1
    h_len = len(h)

    while True and h_len:
        child_id1 = parent_id * 2
        child_id2 = child_id1 + 1

        if 0 < child_id1 <= h_len:
            child_id1_value = h[child_id1-1]
        else:
            child_id1_value = None

        if 0 < child_id2 <= h_len:
            child_id2_value = h[child_id2-1]
        else:
            child_id2_value = None

        parent_value = h[parent_id - 1]

        if all([child_id1_value, child_id2_value]):
            if child_id1_value >= child_id2_value:
                max_id = child_id1
            else:
                max_id = child_id2

            if parent_value < h[max_id-1]:
                h[parent_id-1] = h[max_id-1]
                h[max_id - 1] = parent_value
                parent_id = max_id
            else:
                break

        if all([child_id1_value is None, child_id2_value is None]):
            break

        if child_id1_value and child_id2_value is None:
            if child_id1_value > parent_value:
                h[parent_id - 1] = child_id1_value
                h[child_id1 - 1] = parent_value
                parent_id = child_id1
            else:
                break

        if child_id2_value and child_id1_value is None:
            if child_id2_value > parent_value:
                h[parent_id - 1] = child_id2_value
                h[child_id2 - 1] = parent_value
                parent_id = child_id2
            else:
                break


def insert(h, x):
    h.append(x)
    sift_up(h)


def extract_max(h):
    if len(h):
        return_val = h[0]
        sift_down(h)
    else:
        return_val = None

    return return_val

#JAVA IMPLEMENTATION
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


def build_heap(l):
    heap_size = len(l)
    for i in reversed(range(0, heap_size // 2)): #int i = heapSize / 2; i >= 0; i--)
        heapify(l, i)


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

