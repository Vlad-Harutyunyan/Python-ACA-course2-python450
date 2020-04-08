import itertools

tempList = [[1,2,3,4],[1,2,3,4,5],[1],[1],[2]]
removeType = int(input('please select removing type 1- remove method , 2- list comprehension , 3 -remove way with minimum symbols: '))
result = []

if removeType == 1  :
    for elem in tempList :
        if not elem in result:
            result.append(elem)
    print('Output ` ',result)
if  removeType == 2 :
    [result.append(item) for item in tempList if item not in result]
    print('Output ` ',result)
if removeType == 3 :
    print(list(set(i if type(i)!=list else tuple(i) for i in tempList)))
