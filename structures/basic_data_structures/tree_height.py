"""
Формат входа. Первая строка содержит натуральное число n. Вторая строка содержит n целых чисел
parent0, . . . , parent_n−1. Для каждого 0 ≤ i ≤ n−1, parent_i — родитель вершины i; если parent_i = −1,
то i является корнем. Гарантируется, что корень ровно один. Гарантируется, что данная последовательность задаёт дерево.
Формат выхода.
Высота дерева.
Ограничения. 1 ≤ n ≤ 10^5
"""


def find_from_list(child, memory, nodes):
    parent = nodes[child]
    parent_original = parent

    if parent in memory:
        return memory[parent]
    height = 0
    while parent != -1:
        child = parent
        parent = nodes[child]
        height += 1
    memory[parent_original] = height
    return height + 1


if __name__ == '__main__':
    nodes = []
    not_leafs = set([])
    memory = {}
    n = input()

    for idx, node in enumerate(input().split()):
        node = int(node)
        nodes.append(node)
        not_leafs.add(node)

    max_height = -1
    for i in range(len(nodes)):
        if i not in not_leafs:
            child = i
            max_height = max(max_height, find_from_list(child, memory, nodes))

    print(max_height)
