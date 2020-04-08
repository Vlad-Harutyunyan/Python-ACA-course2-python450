number = int(input('please enter number : '))
checkingType = int(input('please select cheking type 1 - with for loop ,  2 - with minimum symbols  '))


if checkingType == 1 :
    result = 0 
    while number > 0 :
        result += number % 10
        number //= 10
    print(result)
if checkingType == 2 :
    print(sum([int(k) for k in str(number)]))
else :
    print('wrong inputs')
