#practical 5
def factorialRec(num):
    return 1 if num == 1 or num == 0 else num * factorialRec(num - 1);

def calc (num):
    factarr=[]
    temp = 1
    while factorialRec(temp) < num :
        temp += 1
        factarr.append(factorialRec(temp))
    result = max(factarr)
    return result

if __name__ == "__main__":
    print(calc(25))