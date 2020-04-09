
def factorialLoop(num):
    summ = 1
    for x in range(1,num+1):
        summ = summ * x
    return summ


def factorialRec(num):
    if num == 1:
        return num
    elif num == 0:
        return 0
    else:
        return num * factorialRec(num - 1)

print(factorialRec(4))
print(factorialLoop(4))
