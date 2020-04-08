inpRange = [64,32]
result = 1
for x in range (1,min(inpRange)+1):
    if inpRange[0] % x == 0 and  inpRange[1] % x  == 0 and x > result :
        result = x
print(result)