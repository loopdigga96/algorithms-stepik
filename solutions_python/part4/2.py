n, W = map(float, input().split())
items = []
#print(n, capacity)
current_weight = 0
outcome = 0.0
for i in range(int(n)):
    w, v = map(float, input().split())
    items.append((w, v))
items = sorted(items, key=lambda t: t[0]/t[1], reverse=True)
#print(items)

for i in items:
    if W == current_weight:
        break
        
     
    #print('remains- ', W - current_weight)
    if i[1] <= (W - current_weight):
        #print('true')
        #print('before')
        #print(current_weight, outcome)
        current_weight += i[1]
        outcome += i[0]
        #print('after')
        #print(current_weight, outcome)
    else:
        #print('false')
        #print('before')
        #print(current_weight, outcome)
        #print(W - current_weight)
        outcome += (W - current_weight) * (i[0]/i[1])
        current_weight = W
        #print('after')
        #print(current_weight, outcome)

print("{0:.3f}".format(outcome))

