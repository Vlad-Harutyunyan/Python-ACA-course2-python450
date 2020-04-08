word = input('please enter word for cheking : ')
chekingType = int(input('please select cheking type 1 - with for loop ,  2 - in one line  '))


if chekingType == 1 :
    for i in range(0, len(word)//2):  
        if word[i] != word[len(word)-i-1]: 
            print('False')
            break
        else:
            print('True')
            break
elif chekingType == 2 :
    print( word == word[::-1] )
else:
    print('wrong inputs')
    