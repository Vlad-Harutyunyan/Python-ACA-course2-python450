def factorialRec(num):
    if num == 1:
        return num
    elif num == 0:
        return 0
    else:
        return num * factorialRec(num - 1)

def calc (num):
    factarr=[]
    temp = 1
    while factorialRec(temp) < num :
        temp += 1
        factarr.append(factorialRec(temp))
    result = max(factarr)
    return result


if __name__ == "__main__":
    print(calc(10))