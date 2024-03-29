if __name__ == "__main__":

    n, W = map(float, input().split())
    items = []
    current_weight = 0
    outcome = 0.0
    for i in range(int(n)):
        w, v = map(float, input().split())
        items.append((w, v))
    items = sorted(items, key=lambda t: t[0]/t[1], reverse=True)

    for i in items:
        if W == current_weight:
            break

        if i[1] <= (W - current_weight):
            current_weight += i[1]
            outcome += i[0]
        else:
            outcome += (W - current_weight) * (i[0]/i[1])
            current_weight = W

    print("{0:.3f}".format(outcome))
