memory = [222, 100, 700, 400, 40]
process = [60, 75, 175, 275, 800]
a = len(memory)
b = len(process)

def firstFit(memorySize, processSize, a, b):
    block = []
    for x in range(0, a): 
        block.append(-1)

    print("Block Number \t Memory Size")  
    for z in range(0, a):
        print(z, "\t\t", memorySize[z])  
    print()
 
    for y in range(0, b): 
        for z in range(0, a): 
            if processSize[y] <= memorySize[z]:
                block[y] = z
                memorySize[z] = -1
                break

    print("Jobs \t Size \t Block number") 
    for y in range(0, b):
        print((y+1), "\t", processSize[y], end="\t\t")
        if block[y] != -1:   
            print(block[y])
        else:
            print("Blocks not allocated")

firstFit(memory, process, a, b) 
    

