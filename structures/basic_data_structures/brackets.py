"""
Формат входа.
Строка s[1 . . . n], состоящая из заглавных и прописных букв латинского алфавита, цифр,
знаков препинания и скобок из множества []{}().
Формат выхода.
Если скобки в s расставлены правильно, выведите строку “Success".
В противном случае выведите индекс (используя индексацию с единицы) первой закрывающей скобки, для которой нет
соответствующей открывающей. Если такой нет, выведите индекс первой открывающей скобки, для которой нет
соответствующей закрывающей.

"""


def check_brackets(brackets):
    opening = ['[', '(', '{']
    closing = [']', ')', '}']
    mapping = dict(zip(opening, closing))
    stack = []
    indexes = []

    for idx, b in enumerate(brackets):
        if b in opening:
            stack.append(b)
            indexes.append(idx + 1)
        elif b in closing:
            if len(stack) == 0:
                return idx + 1
            else:
                top = stack.pop()
                last_index = indexes.pop()

            if mapping[top] != b:
                return idx + 1

    if len(stack) == 0:
        return 0
    else:
        return indexes.pop()


if __name__ == '__main__':
    brackets = input()
    result = check_brackets(brackets)

    if result == 0:
        print('Success')
    else:
        print(result)
