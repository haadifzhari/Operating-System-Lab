memory = [50, 30, 700, 200, 900]
process = [20, 200, 500, 50]
  
block = []
for x in range(0, len(memory)): 
    block.append(-1)

print("Block Number \t Memory Size")  
for z in range(0, len(memory)):
    print(z, "\t\t", memory[z])  
print()
 
for y in range(0, len(process)): 
    for z in range(0, len(memory)): 
        if process[y] <= memory[z]:
            block[y] = z
            count = 0
            for f in range(0, len(memory)):
                if memory[z] > memory[f] and process[y] <= memory[f]:
                    block[y] = f
                    memory[f] = -1
                    count = 1
                    break
            if count == 0:
                memory[z] = -1
            break

print("Jobs \t Size \t Block number") 
for y in range(0, len(process)):
    print((y+1), "\t", process[y], end="\t\t")
    if block[y] != -1:   
        print(block[y])
    else:
        print("Blocks not allocated")

        

        