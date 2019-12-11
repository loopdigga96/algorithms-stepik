if __name__ == "__main__":
    k, l = map(int, input().split())
    m = {}

    for _ in range(k):
        letter, code = input().split()
        letter = letter[0]
        m[letter] = code

    coded_str = input()

    while coded_str:
        for char, code in m.items():
            if coded_str.startswith(code):
                print(char, end='')
                code_len = len(code)
                coded_str = coded_str[code_len:]
                continue