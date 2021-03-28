memory = [50, 30, 700, 200, 900]
process = [20, 200, 500, 50]
a = len(memory)
b = len(process)
  
def bestFit(memorySize, processSize, a, b):
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
                count = 0
                for f in range(0, a):
                    if memorySize[z] > memorySize[f] and processSize[y] <= memorySize[f]:
                        block[y] = f
                        memorySize[f] = -1
                        count = 1
                        break
                if count == 0:
                    memorySize[z] = -1
                break

    print("Jobs \t Size \t Block number") 
    for y in range(0, b):
        print((y+1), "\t", processSize[y], end="\t\t")
        if block[y] != -1:   
            print(block[y])
        else:
            print("Blocks not allocated")

bestFit(memory, process, a, b)        

 
        