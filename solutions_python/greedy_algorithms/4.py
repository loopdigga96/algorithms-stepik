from collections import Counter


class Node:
    def __init__(self, left=None, right=None, is_leaf=False, value=None, char=None,
                 left_chars=None, right_chars=None):
        self.is_leaf = is_leaf
        self.left = left
        self.right = right
        self.value = value
        self.char = char
        self.left_chars = left_chars
        self.right_chars = right_chars

        if left_chars is not None and right_chars is not None:
            self.under_chars = left_chars + right_chars
        elif left_chars is not None and right_chars is None:
            self.under_chars = left_chars
        elif left_chars is None and right_chars is not None:
            self.under_chars = right_chars
        else:
            self.under_chars = None


def extract_min(h):
    if len(h) >= 1:
        min = h[0]
        del h[0]
    else:
        min = None
    return min


def insert_min(h, n):
    h_len = len(h)
    for idx, member in enumerate(reversed(h)):
        if n.value >= member.value:
            h.insert(h_len-idx, n)
            break
    if h_len == len(h):
        h.insert(0, n)


def update_map(mapping_rules, chars, code):
    for c in chars:
        mapping_rules[c] = f"{code}{mapping_rules[c]}"


def code_string(s, mapping_rules):
    coded_string = []

    for c in s:
        coded_string.append(mapping_rules[c])

    return ''.join(coded_string)


if __name__ == "__main__":
    #s = 'abacabad'
    #s = 'beep boop beer!'
    s = input()
    c = Counter(s)
    c = sorted([tuple([k, c[k]]) for k in c], key=lambda x: x[1])
    f = [pair[1] for pair in c]
    chars = [pair[0] for pair in c]
    n = len(f)
    h = []
    tree = None

    mapping_rules = {pair[0]: '' for pair in c}

    for i in range(len(f)):
        h.append(Node(is_leaf=True, value=f[i], char=[chars[i]]))

    while len(h) >= 1:
        first_min = extract_min(h)
        second_min = extract_min(h)

        if second_min is None:
            if first_min.is_leaf:
                accum_freq = first_min.value
                left_chars = first_min.char
                new_node = Node(value=accum_freq, left=first_min, right=None, left_chars=left_chars)
                tree = new_node
                update_map(mapping_rules, new_node.left_chars, '0')
            else:
                tree = first_min
        else:
            accum_freq = first_min.value + second_min.value

            if first_min.is_leaf:
                left_chars = first_min.char
            else:
                left_chars = first_min.under_chars

            if second_min.is_leaf:
                right_chars = second_min.char
            else:
                right_chars = second_min.under_chars

            new_node = Node(value=accum_freq, left=first_min, right=second_min,
                            left_chars=left_chars, right_chars=right_chars)

            if len(h):
                insert_min(h, new_node)
            else:
                tree = new_node

            update_map(mapping_rules, new_node.left_chars, '0')
            update_map(mapping_rules, new_node.right_chars, '1')

    coded_string = code_string(s, mapping_rules)
    print(len(mapping_rules), len(coded_string))

    for k in mapping_rules:
        print(f'{k}: {mapping_rules[k]}')

    #print(mapping_rules)
    print(coded_string)


