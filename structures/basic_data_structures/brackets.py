def check_brackets(brackets):
    opening = ['[', '(', '{']
    closing = [']', ')', '}']
    stack = []

    for b in brackets:
        if b in opening:
            stack.append(b)
        else:
            if len(stack) == 0:
                return False
            top = stack.pop()

            if any([top == pair[0] and b != pair[1] for pair in zip(opening, closing)]):
                return False

    return True


if __name__ == '__main__':
    brackets = input()
    result = check_brackets(brackets)

    if result:
        print('Success')
    else:
        print(len(brackets))
