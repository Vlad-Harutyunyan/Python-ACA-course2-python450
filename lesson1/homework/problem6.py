
#solution with recursion 
def recFunction (inpRange,n=1,res=1) :
    if n == min(inpRange)+1:
        return res
    else :
        if inpRange[0] % n == 0 and  inpRange[1] % n == 0 and n > res :
            return recFunction(inpRange,n+1,n)
        else :
            return recFunction(inpRange,n+1,res)
         

if __name__ == '__main__':
    #solution without recursion
    result = 1
    inpRange = [64,32]

    for x in range (1,min(inpRange)+1):
        if inpRange[0] % x == 0 and  inpRange[1] % x  == 0 and x > result :
            result = x
    print(result)
    print(recFunction(inpRange))