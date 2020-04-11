number = int(input('please enter number : '))
checkingType = int(input('please select cheking type 1 - with for loop ,  2 - with minimum symbols  '))

def type2(numm):
    return sum([int(k) for k in str(number)])


if checkingType == 1 :
    result = 0 
    while number > 0 :
        result += number % 10
        number //= 10
    print(result)

if checkingType == 2 :
    print(type2(number))

else :
    print('wrong inputs')

#FIXED