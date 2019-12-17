import sys

sys.setrecursionlimit(20000)


def find(child, tree, memory):
    height = 1
    if child not in memory:
        memory[child] = height
        return height
    elif memory[child] != -1:
        return memory[child]
    else:
        # TODO: optimize this loop
        for c, p in enumerate(tree):
            if tree[c] == child:
                if c in memory and memory[c] != -1:
                    compare_height = memory[c] + 1
                else:
                    compare_height = find(c, tree, memory) + 1
                height = max(height, compare_height)
        memory[child] = height
        return height


if __name__ == '__main__':
    n = input()
    nodes = []
    memory = {}
    root = None

    for idx, node in enumerate(map(int, input().split())):
        nodes.append(node)
        memory[node] = -1

        if node == -1:
            root = idx

    for c, p in enumerate(nodes):
        height = find(c, nodes, memory)

    print(memory[root])
