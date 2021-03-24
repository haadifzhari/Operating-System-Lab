memory = [222, 100, 700, 400, 40]
process = [60, 75, 175, 275, 800]

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
            memory[z] = -1
            break

print("Jobs \t Size \t Block number") 
for y in range(0, len(process)):
    print((y+1), "\t", process[y], end="\t\t")
    if block[y] != -1:       
        print(block[y])
    else:
        print("Blocks not allocated")
    

