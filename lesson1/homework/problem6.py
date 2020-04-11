def problem6(a, b):
    if b != 0:
        if a > b:
            return problem6(b, a % b)
        elif a < b:
            return problem6(a, b % a)
    return a
 
if __name__ == '__main__':
    #solution without recursion
    inpRange = [64,32]
    print(problem6(inpRange[0],inpRange[1]))

#FIXED