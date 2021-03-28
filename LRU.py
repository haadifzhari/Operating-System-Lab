reference = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 1, 2, 0]

temp = []#page frame is 3

def lruPlacement(x):
    block = []
    for n in range(x-1, -1, -1):
        current = reference[n] in block
        if len(block)<=3 and not current:
            block.append(reference[n])
    else:
        for i in range(len(temp)):
            if temp[i] == block[2]:
                temp[i] = reference[x]
                break
        print(temp)

for x in range(len(reference)): #0-4
    exists = reference[x] in temp
    if exists:
        print(temp, "hit")
    else:
        if len(temp)<3:
            temp.append(reference[x])
            print(temp)
        else:
            lruPlacement(x)